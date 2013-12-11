#!/bin/bash
CMD="gnome-open $(rospack find documentation_reem_robocup_pkg)/_build/html/index.html"
echo "Running '$CMD'"
$CMD
