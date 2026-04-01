#!/bin/sh
find /lastchaos/server -name 'run' -o -name 'run2' -o -name 'start' -o -name 'start2' | xargs sed -i 's/\r$//'
find /lastchaos/server_run -name '*.py' -o -name '*.sh' | xargs sed -i 's/\r$//'
