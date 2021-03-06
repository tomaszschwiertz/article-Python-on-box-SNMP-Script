import jcs

def main():

    snmp_action = jcs.get_snmp_action()
    snmp_oid = jcs.get_snmp_oid()

    jcs.syslog("8", "snmp_action = ", snmp_action, " snmp_oid = ", snmp_oid)

    if snmp_action == 'get':
        if snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1.1':
            jcs.emit_snmp_attributes(snmp_oid, "String", "Hello World")
        elif snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1.2':
            jcs.emit_snmp_attributes(snmp_oid, "String", "Hello Earth")

if __name__ == '__main__':
    main()
