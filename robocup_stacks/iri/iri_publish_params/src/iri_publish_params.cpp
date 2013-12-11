#include <iri_publish_params.h>
#include <iri_publish_params/classifier_update_service.h>

template <class T>
bool from_string(T& t, 
                 const std::string& s, 
                 std::ios_base& (*f)(std::ios_base&))
{
  std::istringstream iss(s);
  return !(iss >> f >> t).fail();
}

void do_fail(char** argv)
{
  //check params
  ROS_ERROR("%s: Insufficient params!\nUsage: %s <params_file> <filter_method> [selected]. If the parameter 'selected' is ommited, it is set=0", argv[0], argv[0]);
  exit(-1);
}


int main(int argc, char *argv[])
{
  int selected=0;
  int filter_method=0;
  std::string row;
  std::string filename;
  ros::init(argc, argv, "classifier_updates_publisher");
  ros::NodeHandle nh;
  ros::NodeHandle pn("~");
  ros::ServiceClient client = nh.serviceClient<iri_publish_params::classifier_update_service>("classifier_update");
  // wait until service is ready
  client.waitForExistence();

  if(argc<3)
  {
    if (! pn.getParam("input_file", filename)) do_fail(argv);
    if (! pn.getParam("selected_centroid", selected)) do_fail(argv);
    if (! pn.getParam("filter_method", filter_method)) do_fail(argv);
  }
  else
  {
    if(argc==4)
    {
      selected=atoi(argv[3]);
    }  
    filter_method=atoi(argv[2]);
    filename=argv[1];
  }

  iri_publish_params::classifier_update_service srv_message;
  srv_message.request.params.selected_centroid = selected;
  srv_message.request.params.filter_method = filter_method;
  
  std::ifstream pf(filename.c_str(), std::ifstream::in);
  if (!pf.is_open())
  {
    ROS_ERROR("%s: File not found!", argv[0]);
    exit(-1);
  }
  while(!pf.eof())
  {
    std::getline(pf,row);

    if (row.empty())
        continue;

    //std::vector<float> float_row;
    iri_publish_params::classifier_params float_row;

    // ROS_INFO("%s", row.c_str());
  
    std::string::size_type lastPos=0;
    std::string::size_type pos = row.find_first_of(" ", lastPos);

    while(std::string::npos != pos || std::string::npos != lastPos)
    {
      std::string param = row.substr(lastPos, pos - lastPos);
      float fparam;
      from_string<float>(fparam,param,std::dec);
      float_row.params.push_back(fparam);

      lastPos = row.find_first_not_of(" ", pos);
      pos = row.find_first_of(" ", lastPos);
    }
    //for(int a=0;a<float_row.params.size();a++)
    //  std::cout<<float_row.params[a]<<" ";
    srv_message.request.params.update_params.push_back(float_row);
    // ROS_INFO("%s", row.c_str());
  }
  pf.close();

  ROS_INFO("Sending params update (%d vectors dim %d, selected=%d method=%d)\n", srv_message.request.params.update_params.size(), 
                                                                                 srv_message.request.params.update_params[0].params.size(),
                                                                                 srv_message.request.params.selected_centroid,
                                                                                 srv_message.request.params.filter_method);

  iri_publish_params::classifier_update_service srv;
  client.call(srv_message);
  ros::spinOnce();

  return 0;
}

