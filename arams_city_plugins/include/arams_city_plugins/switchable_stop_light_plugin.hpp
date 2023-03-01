#ifndef ARAMS_CITY_PLUGINS__SWITCHABLE_STOP_LIGHT_PLUGIN_H
#define ARAMS_CITY_PLUGINS__SWITCHABLE_STOP_LIGHT_PLUGIN_H

#include <gazebo/common/Plugin.hh>
#include <gazebo/transport/transport.hh>
#include <rclcpp/rclcpp.hpp>
#include <arams_city_plugin_interfaces/srv/set_stop_light_color.hpp>
#include <arams_city_plugin_interfaces/msg/stop_light_color.hpp>

namespace arams_city_plugins {

class SwitchableStopLightPlugin : public gazebo::ModelPlugin
{
public:
  SwitchableStopLightPlugin();
  void Load(gazebo::physics::ModelPtr model, sdf::ElementPtr sdf);

private:
  void setColor(const std::shared_ptr<arams_city_plugin_interfaces::srv::SetStopLightColor::Request> request, std::shared_ptr<arams_city_plugin_interfaces::srv::SetStopLightColor::Response> response);

  std::vector<std::string> managed_lights_;
  std::map<std::string, arams_city_plugin_interfaces::msg::StopLightColor::_data_type> light_bitmask_;

  gazebo::physics::ModelPtr model_;

  gazebo::transport::NodePtr node_;
  gazebo::transport::PublisherPtr vis_pub_;

  rclcpp::Node::SharedPtr ros_node_;
  rclcpp::Service<arams_city_plugin_interfaces::srv::SetStopLightColor>::SharedPtr service_;

};

}

#endif
