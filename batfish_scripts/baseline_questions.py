from pybatfish.client.commands import bf_init_snapshot, bf_session, bf_set_network
from pybatfish.question.question import load_questions
from pybatfish.question import bfq


bf_address = "192.168.56.101"
snapshot_path = "snapshot"
output_acl_rules = "snapshot\\output\\acl_rules"
output_config_properties = "snapshot\\output\\config_properties"
output_ipsec_tunnels = "snapshot\\output\\ipsec_tunnels"
output_packet_forwarding = "snapshot\\output\\packet_forwarding"
output_routing_protocols = "snapshot\\output\\routing_protocols"
output_routing_tables = "snapshot\\output\\routing_tables"
output_topology = "snapshot\\output\\topology"


if __name__ == "__main__":
    bf_session.host = bf_address
    network_name = input("Provide a network name: ")
    snapshot_name = input("Provide a snapshot name: ")
    bf_set_network(network_name)
    bf_init_snapshot(snapshot_path, name=snapshot_name, overwrite=True)
    load_questions()

    """
    Configuration Properties:
    - 15 Questions
    """
    result = bfq.nodeProperties().answer().frame()
    result.to_csv(f"{output_config_properties}/nodeProperties.csv")

    result = bfq.interfaceProperties().answer().frame()
    result.to_csv(f"{output_config_properties}/interfaceProperties.csv")

    result = bfq.bgpProcessConfiguration().answer().frame()
    result.to_csv(f"{output_config_properties}/bgpProcessConfiguration.csv")

    result = bfq.bgpPeerConfiguration().answer().frame()
    result.to_csv(f"{output_config_properties}/bgpPeerConfiguration.csv")

    result = bfq.ospfProcessConfiguration().answer().frame()
    result.to_csv(f"{output_config_properties}/ospfProcessConfiguration.csv")

    result = bfq.ospfInterfaceConfiguration().answer().frame()
    result.to_csv(f"{output_config_properties}/ospfInterfaceConfiguration.csv")
    
    result = bfq.ospfAreaConfiguration().answer().frame()
    result.to_csv(f"{output_config_properties}/ospfAreaConfiguration.csv")
    
    result = bfq.mlagProperties().answer().frame()
    result.to_csv(f"{output_config_properties}/mlagProperties.csv")
    
    result = bfq.ipOwners().answer().frame()
    result.to_csv(f"{output_config_properties}/ipOwners.csv")
    
    # WARNING: If this file is too large, don't open it!
    result = bfq.namedStructures().answer().frame()
    result.to_csv(f"{output_config_properties}/namedStructures.csv")
    
    result = bfq.definedStructures().answer().frame()
    result.to_csv(f"{output_config_properties}/definedStructures.csv")
    
    result = bfq.referencedStructures().answer().frame()
    result.to_csv(f"{output_config_properties}/referencedStructures.csv")
    
    result = bfq.undefinedReferences().answer().frame()
    result.to_csv(f"{output_config_properties}/undefinedReferences.csv")
    
    result = bfq.unusedStructures().answer().frame()
    result.to_csv(f"{output_config_properties}/unusedStructures.csv")
    
    result = bfq.switchedVlanProperties().answer().frame()
    result.to_csv(f"{output_config_properties}/switchedVlanProperties.csv")


    """
    Topology:
    - 1 Question
    """
    result = bfq.layer3Edges().answer().frame()
    result.to_csv(f"{output_topology}/layer3Edges.csv")
    
    
    """
    Routing Protocols:
    - 5 Questions

    Options:
    result = bfq.testRoutePolicies(policies='/as1_to_/', direction='in',
        inputRoutes=list([BgpRoute(network='10.0.0.0/24', originatorIp='4.4.4.4',
        originType='egp', protocol='bgp', asPath=[[64512, 64513], [64514]],
        communities=['64512:42', '64513:21'])])).answer().frame()
    
    result = bfq.searchRoutePolicies(nodes='/^as1/', policies='/as1_to_/',
        inputConstraints=BgpRouteConstraints(prefix=["10.0.0.0/8:8-32",
        "172.16.0.0/28:28-32", "192.168.0.0/16:16-32"]), action='permit').answer().frame()
    """
    result = bfq.bgpSessionCompatibility().answer().frame()
    result.to_csv(f"{output_routing_protocols}/bgpSessionCompatibility.csv")

    result = bfq.bgpSessionStatus().answer().frame()
    result.to_csv(f"{output_routing_protocols}/bgpSessionStatus.csv")
    
    result = bfq.bgpEdges().answer().frame()
    result.to_csv(f"{output_routing_protocols}/bgpEdges.csv")
    
    result = bfq.ospfSessionCompatibility().answer().frame()
    result.to_csv(f"{output_routing_protocols}/ospfSessionCompatibility.csv")
    
    result = bfq.ospfEdges().answer().frame()
    result.to_csv(f"{output_routing_protocols}/ospfEdges.csv")


    """
    Routing and Forwarding Tables
    - 2 Questions

    Options:
    result = bfq.lpmRoutes(ip='2.34.201.10').answer().frame()
    """
    result = bfq.routes().answer().frame()
    result.to_csv(f"{output_routing_tables}/routes.csv")

    result = bfq.bgpRib().answer().frame()
    result.to_csv(f"{output_routing_tables}/bgpRib.csv")

    result = bfq.evpnRib().answer().frame()
    result.to_csv(f"{output_routing_tables}/evpnRib.csv")


    """
    Packet Forwarding
    - 3 Questions

    Options:
    result = bfq.traceroute(startLocation='@enter(as2border1[GigabitEthernet2/0])',
        headers=HeaderConstraints(dstIps='2.34.201.10', srcIps='8.8.8.8')).answer().frame()
    
    result = result = bfq.bidirectionalTraceroute(startLocation='@enter(as2border1[GigabitEthernet2/0])',
        headers=HeaderConstraints(dstIps='2.34.201.10', srcIps='8.8.8.8')).answer().frame()

    result = bfq.reachability(pathConstraints=PathConstraints(startLocation = '/as2/'),
        headers=HeaderConstraints(dstIps='host1', srcIps='0.0.0.0/0', applications='DNS'),
        actions='SUCCESS').answer().frame()
    
    result = bfq.bidirectionalReachability(pathConstraints=PathConstraints(startLocation = '/as2dist1/'),
        headers=HeaderConstraints(dstIps='host1', srcIps='0.0.0.0/0', applications='DNS'),
        returnFlowType='SUCCESS').answer().frame()
    """
    result = bfq.detectLoops().answer().frame()
    result.to_csv(f"{output_packet_forwarding}/detectLoops.csv")

    result = bfq.subnetMultipathConsistency().answer().frame()
    result.to_csv(f"{output_packet_forwarding}/subnetMultipathConsistency.csv")

    result = bfq.loopbackMultipathConsistency().answer().frame()
    result.to_csv(f"{output_packet_forwarding}/loopbackMultipathConsistency.csv")


    """
    Access-lists and firewall rules
    - 1 Question
    
    Options:
    result = bfq.searchFilters(headers=HeaderConstraints(srcIps='10.10.10.0/24',
        dstIps='218.8.104.58', applications = ['dns']), action='deny',
        filters='acl_in').answer().frame()

    result = bfq.testFilters(headers=HeaderConstraints(srcIps='10.10.10.1',
        dstIps='218.8.104.58', applications = ['dns']), nodes='rtr-with-acl',
        filters='acl_in').answer().frame()
    
    result = bfq.findMatchingFilterLines(headers=HeaderConstraints(applications='DNS')).answer().frame()
    """
    result = bfq.filterLineReachability().answer().frame()
    result.to_csv(f"{output_acl_rules}/filterLineReachability.csv")


    """
    IPSec Tunnels
    - 2 Questions
    """
    result = bfq.ipsecSessionStatus().answer().frame()
    result.to_csv(f"{output_ipsec_tunnels}/ipsecSessionStatus.csv")
    
    result = bfq.ipsecEdges().answer().frame()
    result.to_csv(f"{output_ipsec_tunnels}/ipsecEdges.csv")
