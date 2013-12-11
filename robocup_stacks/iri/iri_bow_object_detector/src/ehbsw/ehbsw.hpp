#include <cstring>
#include <cmath>
#include <cstdlib>

#include <iostream>
using namespace std;



//first version of integral histograms
class EHBSW
{
protected:
  const int* I_pu;
  float *Iout_pf; // output map
  int* wavefront1_pu;
  int* wavefront2_pu;
  float* thehist_pu;
  int w_u;
  int h_u;
  int hs_u; //half_win_size
  int vs_u; //vocabulary_size


  int x_u; 
  int y_u;

  void initline(int y_line)
  {
    memset(wavefront1_pu,0,vs_u*sizeof(int));
    memset(wavefront2_pu,0,vs_u*sizeof(int));
    //memset(thehist_pu,0,(vs_u+1)*sizeof(int));
    x_u=hs_u;
    for(int j=y_line-hs_u; j<=y_line+hs_u; j++)
    {
      for(int i=0; i<2*hs_u+1; i++)
      {
	++(wavefront1_pu[I_pu[i+w_u*j]]);
      }
    }
    for(int k=0; k<vs_u; k++)
    {
      thehist_pu[k]=wavefront1_pu[k];
    }
    this->process_hist();
  }
    
  // no check!
  void advance_one()
  {
    x_u++;
    int i1=x_u + hs_u;
    int i2=x_u - hs_u - 1;
    for(int j=y_u-hs_u; j<=y_u+hs_u; j++)
    {
      wavefront1_pu[I_pu[i1+w_u*j]]++;
      wavefront2_pu[I_pu[i2+w_u*j]]++;
    }
    
    //  int g=0;
    //  for(int j=y_u-hs_u; j<=y_u+hs_u; j++, g++)
    //    cout<<"("<<i1<<","<<j<<")"<<I_pu[i1+w_u*j]<<",";
    //  cout<<endl;
    //  g=0;
    //  for(int j=y_u-hs_u; j<=y_u+hs_u; j++,g++)
    //    cout<<"("<<i2<<","<<j<<")"<<I_pu[i2+w_u*j]<<",";
    // cout<<endl;

    for(int k=0; k<vs_u; k++) 
    {
      thehist_pu[k]=wavefront1_pu[k]-wavefront2_pu[k];
      //cout<<thehist_pu[k]<<",";
    }
    //cout<<thehist_pu[vs_u]<<endl<<endl;
    this->process_hist();
  }
  
  virtual void process_hist() = 0;

public:
  /**
     Iin=words map, win=width, hin=height, hsin=half window side (s=2*hsin+1), vs=vocabulary size
  */
  EHBSW(float* Ioutin, int* Iin, int win, int hin, int hsin, int vsin):w_u(win),h_u(hin),hs_u(hsin)
  {
    vs_u=vsin+1; //+1 to account for empty pos
    Iout_pf=Ioutin;
    memset(Iout_pf,0,win*hin*sizeof(float));
    //I_pu=new int[win*hin];
    //memcpy(I_pu, Iin, win*hin*sizeof(int));
    I_pu=Iin;
    wavefront1_pu=new int[vs_u]; //these do not need the bias val
    wavefront2_pu=new int[vs_u]; // -- " --
    thehist_pu=new float[vs_u+1]; //+1 account for empty bin + bias
    thehist_pu[vs_u] = 1.0; //should never be changed (bias)
    //this->initline(this->hs);
    
    //init hist    
    //x_u=hs_u;
    //y_u=hs_u; 
  }

  EHBSW(const EHBSW& a);
  
  ~EHBSW()
  {
    delete [] wavefront1_pu;
    delete [] wavefront2_pu;
    delete [] thehist_pu;
    //delete [] I_pu;
  }

  void run_image()
  {

    for(y_u=hs_u; y_u<h_u-hs_u; y_u++)
    {
      this->initline(y_u);
      for(int i=hs_u+1; i<w_u-hs_u; i++)//first is already done
      {
	this->advance_one();
      }
    }
  }

};

  
class EHBSW_PowNorm : public EHBSW //for now alpha=0.5 AND for logistic regression
{
private:
  const float* classifier_pf;
  
  void process_hist()
  {

    //L2 norm |sqrt(x)|_2 == sqrt(|x|_1)  
    float N=0; //(this->hs*2+1)*(this->hs*2+1); // assuming no missing
    // points. Could be solved
    // with a fallback bin for
    // illegal descs.
    float score=0;
    for (int v=0; v<vs_u; v++) //+1 for the zero (empty)
    {
      //cout<<"("<<thehist_pu[v+1]<<","<<classifier_pf[v]<<")";
      score += sqrt(thehist_pu[v+1])*classifier_pf[v]; //v+1 to skip empty val
      N += thehist_pu[v+1];
    }
    //cout<<endl;
    //cout<<x_u<<" "<<y_u<<" "<<N<<endl;
    N=sqrt(N);
    if (x_u<hs_u || x_u>w_u-hs_u)
      cout<<"alarm! "<<x_u<<endl;
    Iout_pf[x_u+y_u*w_u]=1.0/(1.0+exp(-score/N));
  }
public:

  EHBSW_PowNorm(float* Ioutin, int* Iin, int win, int hin, int hsin, int vsin, float* c): EHBSW(Ioutin, Iin, win, hin, hsin, vsin)
  {
    //classifier_pf=new float[vsin];
    //memcpy(classifier_pf,c, vs_u*sizeof(float));
    classifier_pf=c;
  }
  
  ~EHBSW_PowNorm()
  {
    //delete [] classifier_pf;
  }
};











//################ DEPRECATED!

class EHBSW_LinHist_L1 : public EHBSW
{
private:
  const float* classifier_pf;
  // TODO --- THIS CLASS IS OUTDATED!!!

  void process_hist()
  {
    //L1 norm
    float N=0;//(this->hs*2+1)*(this->hs*2+1); // assuming no missing
    // points. Could be solved
    // with a fallback bin for
    // illegal descs.
    float score=0;
    for (int v=0; v<vs_u; v++) //+1 accounts for bias
    {
      //cout<<thehist_pu[v]<<",";
      score += thehist_pu[v]*classifier_pf[v]; //v+1 to skip empty line //re-add +1 in hist[v<-]
      N += thehist_pu[v];
    }
    //cout<<endl;
    //cout<<x_u<<" "<<y_u<<" "<<w_u<<endl;
    Iout_pf[x_u+y_u*w_u]=score/N;
  }
public:

  EHBSW_LinHist_L1(float* Ioutin, int* Iin, int win, int hin, int hsin, int vsin, float* c): EHBSW(Ioutin, Iin, win, hin, hsin, vsin)
  {
    //classifier_pf=new float[vsin];
    //memcpy(classifier_pf,c, vs_u*sizeof(float));
    classifier_pf=c;
  }
  
  ~EHBSW_LinHist_L1()
  {
    //delete [] classifier_pf;
  }
};
