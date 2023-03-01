#include <arams_city_plugins/switchable_stop_light_plugin.hpp>
#include <gazebo_ros/node.hpp>
#include <gazebo/physics/PhysicsTypes.hh>
#include <gazebo/physics/Model.hh>
#include <gazebo/physics/Link.hh>

namespace arams_city_plugins {

SwitchableStopLightPlugin::SwitchableStopLightPlugin() {}

void SwitchableStopLightPlugin::Load(gazebo::physics::ModelPtr model, sdf::ElementPtr sdf) {
  if(sdf->HasElement("StopLight")) {
    sdf::ElementPtr light_elem = sdf->GetElement("StopLight");
    while (light_elem)
    {
      managed_lights_.push_back("::" +  light_elem->Get<std::string>("name"));
      light_elem = light_elem->GetNextElement("StopLight");
    }
  } else {
    managed_lights_.push_back("");
  }

  light_bitmask_.insert(std::make_pair("green", arams_city_plugin_interfaces::msg::StopLightColor::GREEN));
  light_bitmask_.insert(std::make_pair("yellow", arams_city_plugin_interfaces::msg::StopLightColor::YELLOW));
  light_bitmask_.insert(std::make_pair("red", arams_city_plugin_interfaces::msg::StopLightColor::RED));

  model_ = model;
  ros_node_ = gazebo_ros::Node::Get(sdf);
  service_ = ros_node_->create_service<arams_city_plugin_interfaces::srv::SetStopLightColor>("~/set_color", std::bind(&SwitchableStopLightPlugin::setColor, this, std::placeholders::_1, std::placeholders::_2));
  node_ = gazebo::transport::NodePtr(new gazebo::transport::Node());
  node_->Init();
  vis_pub_ = node_->Advertise<gazebo::msgs::Visual>("/gazebo/default/visual");
}

void SwitchableStopLightPlugin::setColor(const std::shared_ptr<arams_city_plugin_interfaces::srv::SetStopLightColor::Request> request, std::shared_ptr<arams_city_plugin_interfaces::srv::SetStopLightColor::Response> response) {
  auto red = std::make_pair(ignition::math::Color::Red, "red");
  auto yellow = std::make_pair( ignition::math::Color::Yellow, "yellow");
  auto green = std::make_pair(ignition::math::Color::Green, "green");
  auto black = ignition::math::Color::Black;

  for(const auto& l : {red, yellow, green}) {

    gazebo::msgs::Visual msg;
    msg.set_type(gazebo::msgs::Visual::VISUAL);
    auto mat = msg.mutable_material();
    if(light_bitmask_[l.second] & request->color.data) {
      gazebo::msgs::Set(mat->mutable_emissive(), l.first);
      gazebo::msgs::Set(mat->mutable_ambient(), l.first);
    } else {
      gazebo::msgs::Set(mat->mutable_emissive(), black);
      gazebo::msgs::Set(mat->mutable_ambient(), black);
    }

    for(const auto& light : managed_lights_) {
      std::string parent = model_->GetName() + light + "::link";
      msg.set_parent_name(parent);
      msg.set_name(parent + "::" + l.second);
      vis_pub_->Publish(msg);
    }
  }
  response->success = true;

}

GZ_REGISTER_MODEL_PLUGIN(SwitchableStopLightPlugin)
}
