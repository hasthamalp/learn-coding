#!/bin/bash
echo "expVar = $expVar"
echo "myVar = $myVar"
export expVar = "Exported variable"
myVar="My variable"

./test_var
expVar = Exported variable
myVar = 

source test_var
expVar = Exported
variable myVar = My variable
