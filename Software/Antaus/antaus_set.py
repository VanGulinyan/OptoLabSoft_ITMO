import antaus as ant

# Global settings
ant.CONTROL(['BASE_DIVIDER', 177]) # Changes base divider, (177...222)
ant.CONTROL(['OUT_DIVIDER', 1]) # Changes output divider, (1...65535)
ant.CONTROL(['RUN']) # Runs system
ant.CONTROL(['POWER_TRIM', 1]) # Attenuation, (1...100)
ant.CONTROL(['SHUTTER', 1]) # Opens shutter
ant.CONTROL(['SHUTTER', 0]) # Closes shutter
ant.CONTROL(['STOP']) # Stops system
ant.CONTROL(['EXIT']) # Closes com-port connection