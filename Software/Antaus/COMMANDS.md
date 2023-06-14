# Commands for Antaus Control and Setting
## Control Commands
### PING
Check connection via COM-Port with Antaus

### RUN
Runs Antaus

### STOP
Stops Antaus

### FAULT_RESET
Resets Antaus errors

### EXIT
Closes COM-port connection with Antaus

### STATE
Shows Antaus current state (Runs, Preparing to run, Stopped, Preparing to stop)

### FAULT_CODE
Returns error code

### OUT_POWER 
Returns out power

### LOCK_STATE
Returns manual lock state

### BASE_FREQ
Returns base freq

### BASE_DIVIDER_MIN
Returns minimal base divider value

### BASE_DIVIDER_MIN
Returns maximal base divider value

## Variable Settings
### SHUTTER
Opens (value = 1) or closes (value = 0) shutter

### POWER_TRIM
Sets out power (1-100%)

### BASE_DIVIDER
Sets base freq divider

### OUT_DIVIDER
Sets out freq divider (1-65000)

### OUT_BURST
Sets number of impulses in package 

### PULSE_DURATION 
Changes pulse duration (in fs)
