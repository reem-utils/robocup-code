#include "ehbsw.hpp"
//#include <fstream>
//#include <time.h>
#include <iostream>
#include <cstring>
#include <cmath>



// void ehbsw_l1(float* scores, int* vw_ima, int width, int height, int half_win_size, int d, float* classifier)
// {
//   EHBSW_LinHist_L1 a(scores, vw_ima, width, height, half_win_size, d, classifier);
//   a.run_image();
// }

void ehbsw_pownorm(float* scores, int dim_out, int* vw_ima, int height, int width, int half_win_size, int d, float* classifier)
{
  std::cout<<width<<"x"<<height<<" "<<scores<<" "<<d<<std::endl;
  std::cout<<classifier[0]<<" "<<classifier[1]<<" "<<classifier[2]<<"("<<d<<")"<<std::endl;
  std::cout<<half_win_size<<std::endl;
  EHBSW_PowNorm a(scores, vw_ima, width, height, half_win_size, d, classifier);
  a.run_image();
}

//void gen_windows()
//{
//}


void create_histograms(float* h, int nmh, int nh, int mh, int* vws, int nvw, int mvw, float* bboxes, int nbboxes, int mbboxes)
{
  //std::cout<<nmh<<" "<<nh<<" "<<mh<<" "<<nvw<<" "<<mvw<<" "<<nbboxes<<" "<<mbboxes<<std::endl;

  memset(h, 0, nmh*sizeof(float)); //cleaning before first use
  for(int i=0; i<nbboxes; i++)
  {
    //std::cout<<"bbox num "<<i<<std::endl;
    float bb_x1 = bboxes[i*mbboxes];
    float bb_y1 = bboxes[i*mbboxes+1];
    float bb_x2 = bboxes[i*mbboxes+2];
    float bb_y2 = bboxes[i*mbboxes+3];
     
    for(int j=0; j<nvw; j++)
    {

      int x = vws[j*mvw];
      int y = vws[j*mvw+1];
      int vw = vws[j*mvw+2];
      //std::cout<<x<<">="<<bb_x1<<" "<<y<<">="<<bb_y1<<" "<<x<<"<="<<bb_x2<<" "<<y<<"<="<<bb_y2<<std::endl;
      if(x>=bb_x1 && x<=bb_x2 && y>=bb_y1 && y<=bb_y2)
	h[vw+i*mh] += 1;
    }
  }
}


void gen_windows(float *bboxes_gw, int nmbboxes_gw, int *used, int xstep, int ystep, int widthmin, int widthmax, int widthstep, float *whratios, int nwhratios, int xmax, int ymax)
{
  int ibbx=0;
  int nbboxes=nmbboxes_gw/4;
  //std::cout<<"nbboxes = "<<nbboxes<<std::endl;
  memset(bboxes_gw, 0, nmbboxes_gw*sizeof(float)); //cleaning before first use
  for(int i=0; i<nwhratios; i++)
  {
    float whr = whratios[i];
    for(float w=widthmin; w<widthmax; w+=widthstep)
    {
      float h=w*whr;
      //std::cout<<h<<" "<<widthmin<<" "<<widthmax<<" "<<widthstep<<" "<<w<<std::endl;
      for(int x=0+w/2; x<xmax-w/2; x+=xstep)
      {
  	for(int y=0+h/2; y<ymax-h/2; y+=ystep)
  	{
  	  bboxes_gw[ibbx*4]=fmax(0.,float(round(x-w/2)));
  	  bboxes_gw[ibbx*4+1]=fmax(0.,float(round(y-h/2)));
  	  bboxes_gw[ibbx*4+2]=fmin(float(round(x+w/2)),xmax-1.);
	  bboxes_gw[ibbx*4+3]=fmin(float(round(y+h/2)),ymax-1.);
	  //std::cout<<".";
	  //std::cout<<x<<" "<<y<<" "<<bboxes_gw[ibbx*4]<<" "<<bboxes_gw[ibbx*4+1]<<" "<<bboxes_gw[ibbx*4+2]<<" "<<bboxes_gw[ibbx*4+3]<<std::endl;
	  ibbx+=1;
	  //std::cout<<ibbx<<std::endl;
  	}
      }
    }
  }
  *used = ibbx;
}


int main(void)
{

  return -100;
}

