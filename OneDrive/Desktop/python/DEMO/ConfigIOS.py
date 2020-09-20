running_configuration = """
hostname R1
!
boot-start-marker
boot-end-marker
!
no aaa new-model
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
redundancy
!
interface GigabitEthernet0/1
 ip address 192.168.12.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/2
 ip address 192.168.13.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
router bgp 1
 bgp log-neighbor-changes
 network 1.1.1.1 mask 255.255.255.255
 neighbor 192.168.12.2 remote-as 2
 neighbor 192.168.13.3 remote-as 3
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!         
ipv6 ioam timestamp
!

control-plane
!
line con 0
line aux 0
line vty 0 4
 login
 transport input none
!
no scheduler allocate
!
end
"""