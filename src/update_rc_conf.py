"""
Update rc.conf:
     read /etc/rc.conf
     if base_service is not present, insert service=YES
     if base_service is present, but value is NO, change to YES
"""
