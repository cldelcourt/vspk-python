# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUMetadatasFetcher

from bambou import NURESTObject


class NUInfrastructureGatewayProfile(NURESTObject):
    """ Represents a InfrastructureGatewayProfile in the VSD

        Notes:
            Represents Infrastructure Gateway Profile
    """

    __rest_name__ = "infrastructuregatewayprofile"
    __resource_name__ = "infrastructuregatewayprofiles"

    
    ## Constants
    
    CONST_SYSTEM_SYNC_WINDOW_NONE = "NONE"
    
    CONST_REMOTE_LOG_MODE_SCP = "SCP"
    
    CONST_UPGRADE_ACTION_UPGRADE_AT_BOOTSTRAPPING = "UPGRADE_AT_BOOTSTRAPPING"
    
    CONST_UPGRADE_ACTION_DOWNLOAD_AND_UPGRADE_AT_WINDOW = "DOWNLOAD_AND_UPGRADE_AT_WINDOW"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_REMOTE_LOG_MODE_RSYSLOG = "RSYSLOG"
    
    CONST_UPGRADE_ACTION_DOWNLOAD_AND_UPGRADE_NOW = "DOWNLOAD_AND_UPGRADE_NOW"
    
    CONST_UPGRADE_ACTION_NONE = "NONE"
    
    CONST_SYSTEM_SYNC_WINDOW_SIX_HOURS = "SIX_HOURS"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_SYSTEM_SYNC_WINDOW_THIRTY_MINUTES = "THIRTY_MINUTES"
    
    CONST_REMOTE_LOG_MODE_DISABLED = "DISABLED"
    
    CONST_REMOTE_LOG_MODE_SFTP = "SFTP"
    
    CONST_SYSTEM_SYNC_WINDOW_TWO_HOURS = "TWO_HOURS"
    
    CONST_UPGRADE_ACTION_DOWNLOAD_ONLY = "DOWNLOAD_ONLY"
    
    CONST_UPGRADE_ACTION_UPGRADE_NOW = "UPGRADE_NOW"
    
    CONST_SYSTEM_SYNC_WINDOW_FOUR_HOURS = "FOUR_HOURS"
    
    CONST_SYSTEM_SYNC_WINDOW_THREE_HOURS = "THREE_HOURS"
    
    CONST_SYSTEM_SYNC_WINDOW_TEN_MINUTES = "TEN_MINUTES"
    
    CONST_SYSTEM_SYNC_WINDOW_FIVE_HOURS = "FIVE_HOURS"
    
    CONST_SYSTEM_SYNC_WINDOW_ONE_HOUR = "ONE_HOUR"
    
    

    def __init__(self, **kwargs):
        """ Initializes a InfrastructureGatewayProfile instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> infrastructuregatewayprofile = NUInfrastructureGatewayProfile(id=u'xxxx-xxx-xxx-xxx', name=u'InfrastructureGatewayProfile')
                >>> infrastructuregatewayprofile = NUInfrastructureGatewayProfile(data=my_dict)
        """

        super(NUInfrastructureGatewayProfile, self).__init__()

        # Read/Write Attributes
        
        self._ntp_server_key = None
        self._ntp_server_key_id = None
        self._controller_less_duration = None
        self._controller_less_enabled = None
        self._datapath_sync_timeout = None
        self._dead_timer = None
        self._dead_timer_enabled = None
        self._description = None
        self._enterprise_id = None
        self._entity_scope = None
        self._external_id = None
        self._flow_eviction_threshold = None
        self._last_updated_by = None
        self._metadata_upgrade_path = None
        self._name = None
        self._proxy_dns_name = None
        self._remote_log_dir_path = None
        self._remote_log_mode = None
        self._remote_log_password = None
        self._remote_log_server_address = None
        self._remote_log_server_port = None
        self._remote_log_username = None
        self._revert_behaviour = None
        self._revert_timer = None
        self._stats_collector_port = None
        self._system_sync_scheduler = None
        self._system_sync_window = None
        self._upgrade_action = None
        self._use_two_factor = None
        
        self.expose_attribute(local_name="ntp_server_key", remote_name="NTPServerKey", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="ntp_server_key_id", remote_name="NTPServerKeyID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_less_duration", remote_name="controllerLessDuration", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="controller_less_enabled", remote_name="controllerLessEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="datapath_sync_timeout", remote_name="datapathSyncTimeout", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dead_timer", remote_name="deadTimer", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="dead_timer_enabled", remote_name="deadTimerEnabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enterprise_id", remote_name="enterpriseID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="flow_eviction_threshold", remote_name="flowEvictionThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="metadata_upgrade_path", remote_name="metadataUpgradePath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="proxy_dns_name", remote_name="proxyDNSName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="remote_log_dir_path", remote_name="remoteLogDirPath", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_mode", remote_name="remoteLogMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'RSYSLOG', u'SCP', u'SFTP'])
        self.expose_attribute(local_name="remote_log_password", remote_name="remoteLogPassword", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_server_address", remote_name="remoteLogServerAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_server_port", remote_name="remoteLogServerPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="remote_log_username", remote_name="remoteLogUsername", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="revert_behaviour", remote_name="revertBehaviour", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="revert_timer", remote_name="revertTimer", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="stats_collector_port", remote_name="statsCollectorPort", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_sync_scheduler", remote_name="systemSyncScheduler", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="system_sync_window", remote_name="systemSyncWindow", attribute_type=str, is_required=False, is_unique=False, choices=[u'FIVE_HOURS', u'FOUR_HOURS', u'NONE', u'ONE_HOUR', u'SIX_HOURS', u'TEN_MINUTES', u'THIRTY_MINUTES', u'THREE_HOURS', u'TWO_HOURS'])
        self.expose_attribute(local_name="upgrade_action", remote_name="upgradeAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'DOWNLOAD_AND_UPGRADE_AT_WINDOW', u'DOWNLOAD_AND_UPGRADE_NOW', u'DOWNLOAD_ONLY', u'NONE', u'UPGRADE_AT_BOOTSTRAPPING', u'UPGRADE_NOW'])
        self.expose_attribute(local_name="use_two_factor", remote_name="useTwoFactor", attribute_type=bool, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ntp_server_key(self):
        """ Get ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        return self._ntp_server_key

    @ntp_server_key.setter
    def ntp_server_key(self, value):
        """ Set ntp_server_key value.

            Notes:
                If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).

                
                This attribute is named `NTPServerKey` in VSD API.
                
        """
        self._ntp_server_key = value

    
    @property
    def ntp_server_key_id(self):
        """ Get ntp_server_key_id value.

            Notes:
                Correspond to the key ID on the NTP server that matches the ntpServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and 0 to specify unused (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        return self._ntp_server_key_id

    @ntp_server_key_id.setter
    def ntp_server_key_id(self, value):
        """ Set ntp_server_key_id value.

            Notes:
                Correspond to the key ID on the NTP server that matches the ntpServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and 0 to specify unused (VSD/NSG only).

                
                This attribute is named `NTPServerKeyID` in VSD API.
                
        """
        self._ntp_server_key_id = value

    
    @property
    def controller_less_duration(self):
        """ Get controller_less_duration value.

            Notes:
                Duration for a controller-less operation (in ISO-duration format).

                
                This attribute is named `controllerLessDuration` in VSD API.
                
        """
        return self._controller_less_duration

    @controller_less_duration.setter
    def controller_less_duration(self, value):
        """ Set controller_less_duration value.

            Notes:
                Duration for a controller-less operation (in ISO-duration format).

                
                This attribute is named `controllerLessDuration` in VSD API.
                
        """
        self._controller_less_duration = value

    
    @property
    def controller_less_enabled(self):
        """ Get controller_less_enabled value.

            Notes:
                Flag to enable controller-less operations.

                
                This attribute is named `controllerLessEnabled` in VSD API.
                
        """
        return self._controller_less_enabled

    @controller_less_enabled.setter
    def controller_less_enabled(self, value):
        """ Set controller_less_enabled value.

            Notes:
                Flag to enable controller-less operations.

                
                This attribute is named `controllerLessEnabled` in VSD API.
                
        """
        self._controller_less_enabled = value

    
    @property
    def datapath_sync_timeout(self):
        """ Get datapath_sync_timeout value.

            Notes:
                Datapath flows sync-time-interval specified in milliseconds (default: 1000)

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        return self._datapath_sync_timeout

    @datapath_sync_timeout.setter
    def datapath_sync_timeout(self, value):
        """ Set datapath_sync_timeout value.

            Notes:
                Datapath flows sync-time-interval specified in milliseconds (default: 1000)

                
                This attribute is named `datapathSyncTimeout` in VSD API.
                
        """
        self._datapath_sync_timeout = value

    
    @property
    def dead_timer(self):
        """ Get dead_timer value.

            Notes:
                Time, in seconds, allowed for a Gateway to be inactive before the VSD revokes its certificates and marks it as untrusted.

                
                This attribute is named `deadTimer` in VSD API.
                
        """
        return self._dead_timer

    @dead_timer.setter
    def dead_timer(self, value):
        """ Set dead_timer value.

            Notes:
                Time, in seconds, allowed for a Gateway to be inactive before the VSD revokes its certificates and marks it as untrusted.

                
                This attribute is named `deadTimer` in VSD API.
                
        """
        self._dead_timer = value

    
    @property
    def dead_timer_enabled(self):
        """ Get dead_timer_enabled value.

            Notes:
                Flag to enable automatic deactivation.

                
                This attribute is named `deadTimerEnabled` in VSD API.
                
        """
        return self._dead_timer_enabled

    @dead_timer_enabled.setter
    def dead_timer_enabled(self, value):
        """ Set dead_timer_enabled value.

            Notes:
                Flag to enable automatic deactivation.

                
                This attribute is named `deadTimerEnabled` in VSD API.
                
        """
        self._dead_timer_enabled = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description of the Profile instance created.

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description of the Profile instance created.

                
        """
        self._description = value

    
    @property
    def enterprise_id(self):
        """ Get enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        """ Set enterprise_id value.

            Notes:
                Enterprise/Organisation associated with this Profile instance.

                
                This attribute is named `enterpriseID` in VSD API.
                
        """
        self._enterprise_id = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    
    @property
    def flow_eviction_threshold(self):
        """ Get flow_eviction_threshold value.

            Notes:
                Number of flows at which eviction from kernel flow table will be triggered (default: 2500)

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        return self._flow_eviction_threshold

    @flow_eviction_threshold.setter
    def flow_eviction_threshold(self, value):
        """ Set flow_eviction_threshold value.

            Notes:
                Number of flows at which eviction from kernel flow table will be triggered (default: 2500)

                
                This attribute is named `flowEvictionThreshold` in VSD API.
                
        """
        self._flow_eviction_threshold = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def metadata_upgrade_path(self):
        """ Get metadata_upgrade_path value.

            Notes:
                Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.

                
                This attribute is named `metadataUpgradePath` in VSD API.
                
        """
        return self._metadata_upgrade_path

    @metadata_upgrade_path.setter
    def metadata_upgrade_path(self, value):
        """ Set metadata_upgrade_path value.

            Notes:
                Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.

                
                This attribute is named `metadataUpgradePath` in VSD API.
                
        """
        self._metadata_upgrade_path = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Infrastructure Profile

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Infrastructure Profile

                
        """
        self._name = value

    
    @property
    def proxy_dns_name(self):
        """ Get proxy_dns_name value.

            Notes:
                Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        return self._proxy_dns_name

    @proxy_dns_name.setter
    def proxy_dns_name(self, value):
        """ Set proxy_dns_name value.

            Notes:
                Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.

                
                This attribute is named `proxyDNSName` in VSD API.
                
        """
        self._proxy_dns_name = value

    
    @property
    def remote_log_dir_path(self):
        """ Get remote_log_dir_path value.

            Notes:
                Path on the remote log server where the logs generated by the NSG are to be stored.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogDirPath` in VSD API.
                
        """
        return self._remote_log_dir_path

    @remote_log_dir_path.setter
    def remote_log_dir_path(self, value):
        """ Set remote_log_dir_path value.

            Notes:
                Path on the remote log server where the logs generated by the NSG are to be stored.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogDirPath` in VSD API.
                
        """
        self._remote_log_dir_path = value

    
    @property
    def remote_log_mode(self):
        """ Get remote_log_mode value.

            Notes:
                Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.

                
                This attribute is named `remoteLogMode` in VSD API.
                
        """
        return self._remote_log_mode

    @remote_log_mode.setter
    def remote_log_mode(self, value):
        """ Set remote_log_mode value.

            Notes:
                Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.

                
                This attribute is named `remoteLogMode` in VSD API.
                
        """
        self._remote_log_mode = value

    
    @property
    def remote_log_password(self):
        """ Get remote_log_password value.

            Notes:
                Password to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogPassword` in VSD API.
                
        """
        return self._remote_log_password

    @remote_log_password.setter
    def remote_log_password(self, value):
        """ Set remote_log_password value.

            Notes:
                Password to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogPassword` in VSD API.
                
        """
        self._remote_log_password = value

    
    @property
    def remote_log_server_address(self):
        """ Get remote_log_server_address value.

            Notes:
                Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.

                
                This attribute is named `remoteLogServerAddress` in VSD API.
                
        """
        return self._remote_log_server_address

    @remote_log_server_address.setter
    def remote_log_server_address(self, value):
        """ Set remote_log_server_address value.

            Notes:
                Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.

                
                This attribute is named `remoteLogServerAddress` in VSD API.
                
        """
        self._remote_log_server_address = value

    
    @property
    def remote_log_server_port(self):
        """ Get remote_log_server_port value.

            Notes:
                Port to be used to access the Remote Syslog server.  By default, this is port 514.

                
                This attribute is named `remoteLogServerPort` in VSD API.
                
        """
        return self._remote_log_server_port

    @remote_log_server_port.setter
    def remote_log_server_port(self, value):
        """ Set remote_log_server_port value.

            Notes:
                Port to be used to access the Remote Syslog server.  By default, this is port 514.

                
                This attribute is named `remoteLogServerPort` in VSD API.
                
        """
        self._remote_log_server_port = value

    
    @property
    def remote_log_username(self):
        """ Get remote_log_username value.

            Notes:
                Username to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogUsername` in VSD API.
                
        """
        return self._remote_log_username

    @remote_log_username.setter
    def remote_log_username(self, value):
        """ Set remote_log_username value.

            Notes:
                Username to be used when accessing the remote log server via SCP or SFTP.  This field is only useful for SCP and SFTP.

                
                This attribute is named `remoteLogUsername` in VSD API.
                
        """
        self._remote_log_username = value

    
    @property
    def revert_behaviour(self):
        """ Get revert_behaviour value.

            Notes:
                Flag to indicate if the VRS-Revertive-Behaviour took place or not.

                
                This attribute is named `revertBehaviour` in VSD API.
                
        """
        return self._revert_behaviour

    @revert_behaviour.setter
    def revert_behaviour(self, value):
        """ Set revert_behaviour value.

            Notes:
                Flag to indicate if the VRS-Revertive-Behaviour took place or not.

                
                This attribute is named `revertBehaviour` in VSD API.
                
        """
        self._revert_behaviour = value

    
    @property
    def revert_timer(self):
        """ Get revert_timer value.

            Notes:
                Duration for VRS-Revertive-Behaviour when Primary-VSC fails, which needs to be configured in NSG.

                
                This attribute is named `revertTimer` in VSD API.
                
        """
        return self._revert_timer

    @revert_timer.setter
    def revert_timer(self, value):
        """ Set revert_timer value.

            Notes:
                Duration for VRS-Revertive-Behaviour when Primary-VSC fails, which needs to be configured in NSG.

                
                This attribute is named `revertTimer` in VSD API.
                
        """
        self._revert_timer = value

    
    @property
    def stats_collector_port(self):
        """ Get stats_collector_port value.

            Notes:
                The port to open by the proxy for stats collector to use

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        return self._stats_collector_port

    @stats_collector_port.setter
    def stats_collector_port(self, value):
        """ Set stats_collector_port value.

            Notes:
                The port to open by the proxy for stats collector to use

                
                This attribute is named `statsCollectorPort` in VSD API.
                
        """
        self._stats_collector_port = value

    
    @property
    def system_sync_scheduler(self):
        """ Get system_sync_scheduler value.

            Notes:
                Time in a Cron format when configuration update are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek

                
                This attribute is named `systemSyncScheduler` in VSD API.
                
        """
        return self._system_sync_scheduler

    @system_sync_scheduler.setter
    def system_sync_scheduler(self, value):
        """ Set system_sync_scheduler value.

            Notes:
                Time in a Cron format when configuration update are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek

                
                This attribute is named `systemSyncScheduler` in VSD API.
                
        """
        self._system_sync_scheduler = value

    
    @property
    def system_sync_window(self):
        """ Get system_sync_window value.

            Notes:
                Length of time, in seconds, given to a Gateway to apply a configuration change.  This property is closely linked to systemSyncScheduler.

                
                This attribute is named `systemSyncWindow` in VSD API.
                
        """
        return self._system_sync_window

    @system_sync_window.setter
    def system_sync_window(self, value):
        """ Set system_sync_window value.

            Notes:
                Length of time, in seconds, given to a Gateway to apply a configuration change.  This property is closely linked to systemSyncScheduler.

                
                This attribute is named `systemSyncWindow` in VSD API.
                
        """
        self._system_sync_window = value

    
    @property
    def upgrade_action(self):
        """ Get upgrade_action value.

            Notes:
                Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.

                
                This attribute is named `upgradeAction` in VSD API.
                
        """
        return self._upgrade_action

    @upgrade_action.setter
    def upgrade_action(self, value):
        """ Set upgrade_action value.

            Notes:
                Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.

                
                This attribute is named `upgradeAction` in VSD API.
                
        """
        self._upgrade_action = value

    
    @property
    def use_two_factor(self):
        """ Get use_two_factor value.

            Notes:
                Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        return self._use_two_factor

    @use_two_factor.setter
    def use_two_factor(self, value):
        """ Set use_two_factor value.

            Notes:
                Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.

                
                This attribute is named `useTwoFactor` in VSD API.
                
        """
        self._use_two_factor = value

    

    