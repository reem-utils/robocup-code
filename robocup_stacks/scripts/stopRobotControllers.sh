#!/bin/bash

rosservice call /Peer_controller_configurator/orocos_controller_stop 'rightArmTorsoController'
#rosservice call /Peer_controller_configurator/orocos_controller_stop 'rightHandController'
rosservice call /Peer_controller_configurator/orocos_controller_stop 'leftArmController'
#rosservice call /Peer_controller_configurator/orocos_controller_stop 'leftHandController'
rosservice call /Peer_controller_configurator/orocos_controller_stop 'headController'
