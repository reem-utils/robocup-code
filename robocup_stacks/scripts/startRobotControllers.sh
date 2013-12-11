#!/bin/bash

rosservice call /Peer_controller_configurator/orocos_controller_start 'rightArmTorsoController'
#rosservice call /Peer_controller_configurator/orocos_controller_start 'rightHandController'
rosservice call /Peer_controller_configurator/orocos_controller_start 'leftArmController'
#rosservice call /Peer_controller_configurator/orocos_controller_start 'leftHandController'
rosservice call /Peer_controller_configurator/orocos_controller_start 'headController'
