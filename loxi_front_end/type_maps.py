# Copyright 2013, Big Switch Networks, Inc.
#
# LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
# the following special exception:
#
# LOXI Exception
#
# As a special exception to the terms of the EPL, you may distribute libraries
# generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
# that copyright and licensing notices generated by LoxiGen are not altered or removed
# from the LoxiGen Libraries and the notice provided below is (i) included in
# the LoxiGen Libraries, if distributed in source code form and (ii) included in any
# documentation for the LoxiGen Libraries, if distributed in binary form.
#
# Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
#
# You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
# a copy of the EPL at:
#
# http://www.eclipse.org/legal/epl-v10.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# EPL for the specific language governing permissions and limitations
# under the EPL.

#
# Miscellaneous type information
#
# Define the map between sub-class types and wire values.  In each
# case, an array indexed by wire version gives a hash from identifier
# to wire value.
#

import of_g
import sys
from generic_utils import *
import oxm
import loxi_utils.loxi_utils as loxi_utils

invalid_type = "invalid_type"
invalid_value = "0xeeee"  # Note, as a string

################################################################
#
# Define type data for inheritance classes:
#   instructions, actions, queue properties and OXM
#
# Messages are not in this group; they're treated specially for now
#
# These are indexed by wire protocol number
#
################################################################

instruction_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),

    # version 1.1
    of_g.VERSION_1_1:dict(
        goto_table = 1,
        write_metadata = 2,
        write_actions = 3,
        apply_actions = 4,
        clear_actions = 5,
        experimenter = 0xffff
        ),

    # version 1.2
    of_g.VERSION_1_2:dict(
        goto_table = 1,
        write_metadata = 2,
        write_actions = 3,
        apply_actions = 4,
        clear_actions = 5,
        experimenter = 0xffff
        ),

    # version 1.3
    of_g.VERSION_1_3:dict(
        goto_table = 1,
        write_metadata = 2,
        write_actions = 3,
        apply_actions = 4,
        clear_actions = 5,
        meter = 6,
        experimenter = 0xffff
        )
    }

of_1_3_action_types = dict(
    output       = 0,
    copy_ttl_out = 11,
    copy_ttl_in  = 12,
    set_mpls_ttl = 15,
    dec_mpls_ttl = 16,
    push_vlan    = 17,
    pop_vlan     = 18,
    push_mpls    = 19,
    pop_mpls     = 20,
    set_queue    = 21,
    group        = 22,
    set_nw_ttl   = 23,
    dec_nw_ttl   = 24,
    set_field    = 25,
    push_pbb     = 26,
    pop_pbb      = 27,
    experimenter = 0xffff,
    bsn_mirror = 0xffff,
    bsn_set_tunnel_dst = 0xffff,
    nicira_dec_ttl = 0xffff
    )

# Indexed by OF version
action_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(
        output = 0,
        set_vlan_vid = 1,
        set_vlan_pcp = 2,
        strip_vlan = 3,
        set_dl_src = 4,
        set_dl_dst = 5,
        set_nw_src = 6,
        set_nw_dst = 7,
        set_nw_tos = 8,
        set_tp_src = 9,
        set_tp_dst = 10,
        enqueue = 11,
        experimenter = 0xffff,
        bsn_mirror = 0xffff,
        bsn_set_tunnel_dst = 0xffff,
        nicira_dec_ttl = 0xffff
        ),

    # version 1.1
    of_g.VERSION_1_1:dict(
        output = 0,
        set_vlan_vid = 1,
        set_vlan_pcp = 2,
        set_dl_src = 3,
        set_dl_dst = 4,
        set_nw_src = 5,
        set_nw_dst = 6,
        set_nw_tos = 7,
        set_nw_ecn = 8,
        set_tp_src = 9,
        set_tp_dst = 10,
        copy_ttl_out = 11,
        copy_ttl_in = 12,
        set_mpls_label = 13,
        set_mpls_tc = 14,
        set_mpls_ttl = 15,
        dec_mpls_ttl = 16,
        push_vlan = 17,
        pop_vlan = 18,
        push_mpls = 19,
        pop_mpls = 20,
        set_queue = 21,
        group = 22,
        set_nw_ttl = 23,
        dec_nw_ttl = 24,
        experimenter = 0xffff,
        bsn_mirror = 0xffff,
        bsn_set_tunnel_dst = 0xffff,
        nicira_dec_ttl = 0xffff
        ),

    # version 1.2
    of_g.VERSION_1_2:dict(
        output       = 0,
        copy_ttl_out = 11,
        copy_ttl_in  = 12,
        set_mpls_ttl = 15,
        dec_mpls_ttl = 16,
        push_vlan    = 17,
        pop_vlan     = 18,
        push_mpls    = 19,
        pop_mpls     = 20,
        set_queue    = 21,
        group        = 22,
        set_nw_ttl   = 23,
        dec_nw_ttl   = 24,
        set_field    = 25,
        experimenter = 0xffff,
        bsn_mirror = 0xffff,
        bsn_set_tunnel_dst = 0xffff,
        nicira_dec_ttl = 0xffff
        ),

    # version 1.3
    of_g.VERSION_1_3:of_1_3_action_types

    }

action_id_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),
    of_g.VERSION_1_1:dict(),
    of_g.VERSION_1_2:dict(),
    of_g.VERSION_1_3:of_1_3_action_types
    }

queue_prop_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(
        min_rate      = 1,
        # experimenter  = 0xffff
        ),
    # version 1.1
    of_g.VERSION_1_1:dict(
        min_rate      = 1,
        #  experimenter  = 0xffff
        ),
    # version 1.2
    of_g.VERSION_1_2:dict(
        min_rate      = 1,
        max_rate      = 2,
        experimenter  = 0xffff
        ),
    # version 1.3
    of_g.VERSION_1_3:dict(
        min_rate      = 1,
        max_rate      = 2,
        experimenter  = 0xffff
        )
    }

oxm_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),

    # version 1.1
    of_g.VERSION_1_1:dict(),

    # version 1.2
    of_g.VERSION_1_2:oxm.oxm_wire_type,

    # version 1.3
    of_g.VERSION_1_3:oxm.oxm_wire_type  # FIXME needs update for 1.3?
    }

hello_elem_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),

    # version 1.1
    of_g.VERSION_1_1:dict(),

    # version 1.2
    of_g.VERSION_1_2:dict(),

    # version 1.3
    of_g.VERSION_1_3:dict(
        versionbitmap = 1
        )
    }

table_feature_prop_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),

    # version 1.1
    of_g.VERSION_1_1:dict(),

    # version 1.2
    of_g.VERSION_1_2:dict(),

    # version 1.3
    of_g.VERSION_1_3:dict(
        instructions           = 0,
        instructions_miss      = 1,
        next_tables            = 2,
        next_tables_miss       = 3,
        write_actions          = 4,
        write_actions_miss     = 5,
        apply_actions          = 6,
        apply_actions_miss     = 7,
        match                  = 8,
        wildcards              = 10,
        write_setfield         = 12,
        write_setfield_miss    = 13,
        apply_setfield         = 14,
        apply_setfield_miss    = 15,
#        experimenter           = 0xFFFE,
#        experimenter_miss      = 0xFFFF,
        experimenter            = 0xFFFF,  # Wrong: should be experimenter_miss
        )
    }

meter_band_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(),

    # version 1.1
    of_g.VERSION_1_1:dict(),

    # version 1.2
    of_g.VERSION_1_2:dict(),

    # version 1.3
    of_g.VERSION_1_3:dict(
        drop                   = 1,
        dscp_remark            = 2,
        experimenter           = 0xFFFF,
        )
    }

# All inheritance data for non-messages
inheritance_data = dict(
    of_instruction = instruction_types,
    of_action = action_types,
    of_action_id = action_id_types,
    of_oxm = oxm_types,
    of_queue_prop = queue_prop_types,
    of_hello_elem = hello_elem_types,
    of_table_feature_prop = table_feature_prop_types,
    of_meter_band = meter_band_types
    )

################################################################
# Now generate the maps from parent to list of subclasses
################################################################

# # These lists have entries which are a fixed type, no inheritance
# fixed_lists = [
#     "of_list_bucket",
#     "of_list_bucket_counter",
#     "of_list_flow_stats_entry",
#     "of_list_group_desc_stats_entry",
#     "of_list_group_stats_entry",
#     "of_list_packet_queue",
#     "of_list_port_desc",
#     "of_list_port_stats_entry",
#     "of_list_queue_stats_entry",
#     "of_list_table_stats_entry"
#     ]

# for cls in fixed_lists:
#     base_type = list_to_entry_type(cls)
#     of_g.inheritance_map[base_type] = [base_type]

inheritance_map = dict()
for parent, versioned in inheritance_data.items():
    inheritance_map[parent] = set()
    for ver, subclasses in versioned.items():
        for subcls in subclasses:
            inheritance_map[parent].add(subcls)

def class_is_virtual(cls):
    """
    Returns True if cls is a virtual class
    """
    if cls in inheritance_map:
        return True
    if cls.find("header") > 0:
        return True
    if loxi_utils.class_is_list(cls):
        return True
    return False

################################################################
#
# These are message types
#
################################################################

message_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(
        hello                   = 0,
        error_msg               = 1,
        echo_request            = 2,
        echo_reply              = 3,
        experimenter            = 4,
        features_request        = 5,
        features_reply          = 6,
        get_config_request      = 7,
        get_config_reply        = 8,
        set_config              = 9,
        packet_in               = 10,
        flow_removed            = 11,
        port_status             = 12,
        packet_out              = 13,
        flow_mod                = 14,
        port_mod                = 15,
        stats_request           = 16,
        stats_reply             = 17,
        barrier_request         = 18,
        barrier_reply           = 19,
        queue_get_config_request = 20,
        queue_get_config_reply  = 21,
        table_mod               = 22    # Unofficial 1.0 extension
        ),

    # version 1.1
    of_g.VERSION_1_1:dict(
        hello                   = 0,
        error_msg               = 1,
        echo_request            = 2,
        echo_reply              = 3,
        experimenter            = 4,
        features_request        = 5,
        features_reply          = 6,
        get_config_request      = 7,
        get_config_reply        = 8,
        set_config              = 9,
        packet_in               = 10,
        flow_removed            = 11,
        port_status             = 12,
        packet_out              = 13,
        flow_mod                = 14,
        group_mod               = 15,
        port_mod                = 16,
        table_mod               = 17,
        stats_request           = 18,
        stats_reply             = 19,
        barrier_request         = 20,
        barrier_reply           = 21,
        queue_get_config_request = 22,
        queue_get_config_reply  = 23
        ),

    # version 1.2
    of_g.VERSION_1_2:dict(
        hello                   = 0,
        error_msg               = 1,
        echo_request            = 2,
        echo_reply              = 3,
        experimenter            = 4,
        features_request        = 5,
        features_reply          = 6,
        get_config_request      = 7,
        get_config_reply        = 8,
        set_config              = 9,
        packet_in               = 10,
        flow_removed            = 11,
        port_status             = 12,
        packet_out              = 13,
        flow_mod                = 14,
        group_mod               = 15,
        port_mod                = 16,
        table_mod               = 17,
        stats_request           = 18,
        stats_reply             = 19,
        barrier_request         = 20,
        barrier_reply           = 21,
        queue_get_config_request = 22,
        queue_get_config_reply   = 23,
        role_request            = 24,
        role_reply              = 25,
        ),

    # version 1.3
    of_g.VERSION_1_3:dict(
        hello                   = 0,
        error_msg               = 1,
        echo_request            = 2,
        echo_reply              = 3,
        experimenter            = 4,
        features_request        = 5,
        features_reply          = 6,
        get_config_request      = 7,
        get_config_reply        = 8,
        set_config              = 9,
        packet_in               = 10,
        flow_removed            = 11,
        port_status             = 12,
        packet_out              = 13,
        flow_mod                = 14,
        group_mod               = 15,
        port_mod                = 16,
        table_mod               = 17,
        stats_request           = 18,  # FIXME Multipart
        stats_reply             = 19,
        barrier_request         = 20,
        barrier_reply           = 21,
        queue_get_config_request = 22,
        queue_get_config_reply   = 23,
        role_request            = 24,
        role_reply              = 25,
        async_get_request       = 26,
        async_get_reply         = 27,
        async_set               = 28,
        meter_mod               = 29
        )
    }

################################################################
#
# These are other objects that have a notion of type but are
# not (yet) promoted to objects with inheritance
#
################################################################

stats_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(
        desc = 0,
        flow = 1,
        aggregate = 2,
        table = 3,
        port = 4,
        queue = 5,
        experimenter = 0xffff
        ),

    # version 1.1
    of_g.VERSION_1_1:dict(
        desc = 0,
        flow = 1,
        aggregate = 2,
        table = 3,
        port = 4,
        queue = 5,
        group = 6,
        group_desc = 7,
        experimenter = 0xffff
        ),

    # version 1.2
        of_g.VERSION_1_2:dict(
        desc = 0,
        flow = 1,
        aggregate = 2,
        table = 3,
        port = 4,
        queue = 5,
        group = 6,
        group_desc = 7,
        group_features = 8,
        experimenter = 0xffff
        ),

    # version 1.3
        of_g.VERSION_1_3:dict(
        desc = 0,
        flow = 1,
        aggregate = 2,
        table = 3,
        port = 4,
        queue = 5,
        group = 6,
        group_desc = 7,
        group_features = 8,
        meter = 9,
        meter_config = 10,
        meter_features = 11,
        table_features = 12,
        port_desc = 13,
        experimenter = 0xffff
        )
    }

common_flow_mod_types = dict(
    add = 0,
    modify = 1,
    modify_strict = 2,
    delete = 3,
    delete_strict = 4
    )

flow_mod_types = {
    # version 1.0
    of_g.VERSION_1_0:common_flow_mod_types,
    of_g.VERSION_1_1:common_flow_mod_types,
    of_g.VERSION_1_2:common_flow_mod_types,
    of_g.VERSION_1_3:common_flow_mod_types
    }

# These do not translate to objects (yet)
error_types = {
    # version 1.0
    of_g.VERSION_1_0:dict(
        hello_failed        = 0,
        bad_request         = 1,
        bad_action          = 2,
        flow_mod_failed     = 3,
        port_mod_failed     = 4,
        queue_op_failed     = 5
        ),

    # version 1.1
    of_g.VERSION_1_1:dict(
        hello_failed         = 0,
        bad_request          = 1,
        bad_action           = 2,
        bad_instruction      = 3,
        bad_match            = 4,
        flow_mod_failed      = 5,
        group_mod_failed     = 6,
        port_mod_failed      = 7,
        table_mod_failed     = 8,
        queue_op_failed      = 9,
        switch_config_failed = 10
        ),

    # version 1.2
    of_g.VERSION_1_2:dict(
        hello_failed         = 0,
        bad_request          = 1,
        bad_action           = 2,
        bad_instruction      = 3,
        bad_match            = 4,
        flow_mod_failed      = 5,
        group_mod_failed     = 6,
        port_mod_failed      = 7,
        table_mod_failed     = 8,
        queue_op_failed      = 9,
        switch_config_failed = 10,
        role_request_failed  = 11,
        experimenter = 0xffff
        ),

    # version 1.3
    of_g.VERSION_1_3:dict(
        hello_failed         = 0,
        bad_request          = 1,
        bad_action           = 2,
        bad_instruction      = 3,
        bad_match            = 4,
        flow_mod_failed      = 5,
        group_mod_failed     = 6,
        port_mod_failed      = 7,
        table_mod_failed     = 8,
        queue_op_failed      = 9,
        switch_config_failed = 10,
        role_request_failed  = 11,
        meter_mod_failed     = 12,
        table_features_failed= 13,
        experimenter = 0xffff
        )
    }

##
# These are the objects whose length is specified by an external
# reference, specifically another data member in the class.
#
#external_length_spec = {
#    ("of_packet_out", "actions", OF_VERSION_1_0) : "actions_len",
#    ("of_packet_out", "actions", OF_VERSION_1_1) : "actions_len",
#    ("of_packet_out", "actions", OF_VERSION_1_2) : "actions_len",
#    ("of_packet_out", "actions", OF_VERSION_1_3) : "actions_len"
#}


################################################################
#
# type_val is the primary data structure that maps an
# (class_name, version) pair to the wire data type value
#
################################################################

type_val = dict()

for version, classes in message_types.items():
    for cls in classes:
        name = "of_" + cls
        type_val[(name, version)] = classes[cls]

for parent, versioned in inheritance_data.items():
    for version, subclasses in versioned.items():
        for subcls, value in subclasses.items():
            name = parent + "_" + subcls
            type_val[(name, version)] = value

# Special case OF-1.2 match type
type_val[("of_match_v3", of_g.VERSION_1_2)] = 0x8000
type_val[("of_match_v3", of_g.VERSION_1_3)] = 0x8000

# Utility function
def dict_to_array(d, m_val, def_val=-1):
    """
    Given a dictionary, d, with each value a small integer,
    produce an array indexed by the integer whose value is the key.
    @param d The dictionary
    @param m_val Ignore values greater than m_val
    @param def_val The default value (for indices not in range of d)
    """

    # Get the max value in range for hash
    max_val = 0
    for key in d:
        if (d[key] > max_val) and (d[key] < m_val):
            max_val = d[key]
    ar = []
    for x in range(0, max_val + 1):
        ar.append(def_val)
    for key in d:
        if (d[key] < m_val):
            ar[d[key]] = key
    return ar

def type_array_len(version_indexed, max_val):
    """
    Given versioned information about a type, calculate how long
    the unified array should be.

    @param version_indexed A dict indexed by version. Each value is a
    dict indexed by a name and whose value is an integer
    @param max_val Ignore values greater than this for length calcs
    """
    # First, find the max length of all arrays
    arr_len = 0
    for version, val_dict in version_indexed.items():
        ar = dict_to_array(val_dict, max_val, invalid_type)
        if arr_len < len(ar):
            arr_len = len(ar)
    return arr_len

# FIXME:  Need to move update for multipart messages

stats_reply_list = [
    "of_aggregate_stats_reply",
    "of_desc_stats_reply",
    "of_experimenter_stats_reply",
    "of_flow_stats_reply",
    "of_group_stats_reply",
    "of_group_desc_stats_reply",
    "of_group_features_stats_reply",
    "of_meter_stats_reply",
    "of_meter_config_stats_reply",
    "of_meter_features_stats_reply",
    "of_port_stats_reply",
    "of_port_desc_stats_reply",
    "of_queue_stats_reply",
    "of_table_stats_reply",
    "of_table_features_stats_reply"
]

stats_request_list = [
    "of_aggregate_stats_request",
    "of_desc_stats_request",
    "of_experimenter_stats_request",
    "of_flow_stats_request",
    "of_group_stats_request",
    "of_group_desc_stats_request",
    "of_group_features_stats_request",
    "of_meter_stats_request",
    "of_meter_config_stats_request",
    "of_meter_features_stats_request",
    "of_port_stats_request",
    "of_port_desc_stats_request",
    "of_queue_stats_request",
    "of_table_stats_request",
    "of_table_features_stats_request"
]

flow_mod_list = [
    "of_flow_add",
    "of_flow_modify",
    "of_flow_modify_strict",
    "of_flow_delete",
    "of_flow_delete_strict"
]

def sub_class_map(base_type, version):
    """
    Returns an iterable object giving the instance nameys and subclass types
    for the base_type, version values
    """
    rv = []
    if base_type not in inheritance_map:
        return rv

    for instance in inheritance_map[base_type]:
        subcls = loxi_utils.instance_to_class(instance, base_type)
        if not loxi_utils.class_in_version(subcls, version):
            continue
        rv.append((instance, subcls))

    return rv

################################################################
#
# Extension related data and functions
#
################################################################

# Per OF Version, per experimenter, map exp msg type (subtype) to object IDs
# @fixme Generate defines for OF_<exp>_SUBTYPE_<msg> for the values below?
extension_message_subtype = {
    # version 1.0
    of_g.VERSION_1_0:dict(  # Version 1.0 extensions
        bsn = {   # BSN extensions; indexed by class name, value is subtype
            "of_bsn_set_ip_mask"             : 0,
            "of_bsn_get_ip_mask_request"     : 1,
            "of_bsn_get_ip_mask_reply"       : 2,
            "of_bsn_set_mirroring"           : 3,
            "of_bsn_get_mirroring_request"   : 4,
            "of_bsn_get_mirroring_reply"     : 5,
            "of_bsn_shell_command"           : 6,
            "of_bsn_shell_output"            : 7,
            "of_bsn_shell_status"            : 8,
            "of_bsn_get_interfaces_request"  : 9,
            "of_bsn_get_interfaces_reply"    : 10,
            "of_bsn_set_pktin_suppression"   : 11,
            "of_bsn_set_l2_table"            : 12,
            "of_bsn_get_l2_table_request"    : 13,
            "of_bsn_get_l2_table_reply"      : 14,
            },
        nicira = {   # Nicira extensions, value is subtype
            "of_nicira_controller_role_request"      : 10,
            "of_nicira_controller_role_reply"        : 11,
            },
        ),
    of_g.VERSION_1_1:dict(  # Version 1.0 extensions
        bsn = {   # BSN extensions; indexed by class name, value is subtype
            "of_bsn_set_mirroring"           : 3,
            "of_bsn_get_mirroring_request"   : 4,
            "of_bsn_get_mirroring_reply"     : 5,
            "of_bsn_get_interfaces_request"  : 9,
            "of_bsn_get_interfaces_reply"    : 10,
            "of_bsn_set_pktin_suppression"   : 11,
            },
        ),
    of_g.VERSION_1_2:dict(  # Version 1.0 extensions
        bsn = {   # BSN extensions; indexed by class name, value is subtype
            "of_bsn_set_mirroring"           : 3,
            "of_bsn_get_mirroring_request"   : 4,
            "of_bsn_get_mirroring_reply"     : 5,
            "of_bsn_get_interfaces_request"  : 9,
            "of_bsn_get_interfaces_reply"    : 10,
            "of_bsn_set_pktin_suppression"   : 11,
            },
        ),
    of_g.VERSION_1_3:dict(  # Version 1.0 extensions
        bsn = {   # BSN extensions; indexed by class name, value is subtype
            "of_bsn_set_mirroring"           : 3,
            "of_bsn_get_mirroring_request"   : 4,
            "of_bsn_get_mirroring_reply"     : 5,
            "of_bsn_get_interfaces_request"  : 9,
            "of_bsn_get_interfaces_reply"    : 10,
            "of_bsn_set_pktin_suppression"   : 11,
            },
        ),
}

# Set to empty dict if no extension actions defined
# Per OF Version, per experimenter, map actions to subtype
extension_action_subtype = {
    # version 1.0
    of_g.VERSION_1_0:dict(  # Version 1.0 extensions
        bsn = {   # of_action_bsn_
            "of_action_bsn_mirror"           : 1,
            "of_action_bsn_set_tunnel_dst"   : 2,
            },
        nicira = {   # of_action_nicira_
            "of_action_nicira_dec_ttl"       : 18,
            }
        ),
    of_g.VERSION_1_1:dict(  # Version 1.0 extensions
        bsn = {   # of_action_bsn_
            "of_action_bsn_mirror"           : 1,
            "of_action_bsn_set_tunnel_dst"   : 2,
            },
        nicira = {   # of_action_nicira_
            "of_action_nicira_dec_ttl"       : 18,
            }
        ),
    of_g.VERSION_1_2:dict(  # Version 1.0 extensions
        bsn = {   # of_action_bsn_
            "of_action_bsn_mirror"           : 1,
            "of_action_bsn_set_tunnel_dst"   : 2,
            },
        nicira = {   # of_action_nicira_
            "of_action_nicira_dec_ttl"       : 18,
            }
        ),
    of_g.VERSION_1_3:dict(  # Version 1.0 extensions
        bsn = {   # of_action_bsn_
            "of_action_bsn_mirror"           : 1,
            "of_action_bsn_set_tunnel_dst"   : 2,
            },
        nicira = {   # of_action_nicira_
            "of_action_nicira_dec_ttl"       : 18,
            }
        ),
}

# Set to empty dict if no extension actions defined
# Per OF Version, per experimenter, map actions to subtype
extension_action_id_subtype = {
    # version 1.0
    of_g.VERSION_1_0:dict(),
    of_g.VERSION_1_1:dict(),
    of_g.VERSION_1_2:dict(),
    of_g.VERSION_1_3:dict(  # Version 1.3 extensions
        bsn = {   # of_action_bsn_
            "of_action_id_bsn_mirror"           : 1,
            "of_action_id_bsn_set_tunnel_dst"   : 2,
            },
        nicira = {   # of_action_nicira_
            "of_action_id_nicira_dec_ttl"       : 18,
            }
        ),
}

# Set to empty dict if no extension instructions defined
extension_instruction_subtype = {}

# Set to empty dict if no extension instructions defined
extension_queue_prop_subtype = {}

# Set to empty dict if no extension instructions defined
extension_table_feature_prop_subtype = {}

extension_objects = [
    extension_message_subtype,
    extension_action_subtype,
    extension_action_id_subtype,
    extension_instruction_subtype,
    extension_queue_prop_subtype,
    extension_table_feature_prop_subtype
]

################################################################
# These are extension type generic (for messages, actions...)
################################################################

def extension_to_experimenter_name(cls):
    """
    Return the name of the experimenter if class is an
    extension, else None

    This is brute force; we search all extension data for a match
    """

    for ext_obj in extension_objects:
        for version, exp_list in ext_obj.items():
            for exp_name, classes in exp_list.items():
                if cls in classes:
                    return exp_name
    return None

def extension_to_experimenter_id(cls):
    """
    Return the ID of the experimenter if class is an
    extension, else None
    """
    exp_name = extension_to_experimenter_name(cls)
    if exp_name:
        return of_g.experimenter_name_to_id[exp_name]
    return None

def extension_to_experimenter_macro_name(cls):
    """
    Return the "macro name" of the ID of the experimenter if class is an
    extension, else None
    """
    exp_name = extension_to_experimenter_name(cls)
    if exp_name:
        return "OF_EXPERIMENTER_ID_" + exp_name.upper()
    return None

def extension_to_subtype(cls, version):
    """
    Generic across all extension objects, return subtype identifier
    """
    for ext_obj in extension_objects:
        for version, exp_list in ext_obj.items():
            for exp_name, classes in exp_list.items():
                if cls in classes:
                    return classes[cls]

def class_is_extension(cls, version):
    """
    Return True if class, version is recognized as an extension
    of any type (message, action....)

    Accepts of_g.OF_VERSION_ANY
    """

    for ext_obj in extension_objects:
        if cls_is_ext_obj(cls, version, ext_obj):
            return True

    return False

# Internal
def cls_is_ext_obj(cls, version, ext_obj):
    """
    @brief Return True if cls in an extension of type ext_obj
    @param cls The class to check
    @param version The version to check
    @param ext_obj The extension object dictionary (messages, actions...)

    Accepts of_g.VERSION_ANY
    """

    # Call with each version if "any" is passed
    if version == of_g.VERSION_ANY:
        for v in of_g.of_version_range:
            if cls_is_ext_obj(cls, v, ext_obj):
                return True
    else:   # Version specified
        if version in ext_obj:
            for exp, subtype_vals in ext_obj[version].items():
                if cls in subtype_vals:
                    return True

    return False

################################################################
# These are extension message specific
################################################################

def message_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an  extension
    This is brute force, searching records for a match
    """
    return cls_is_ext_obj(cls, version, extension_message_subtype)

def extension_message_to_subtype(cls, version):
    """
    Return the subtype of the experimenter message if the class is an
    extension, else None
    """
    if version in extension_message_subtype:
        for exp, classes in extension_message_subtype[version].items():
            for ext_class, subtype in classes.items():
                if cls == ext_class:
                    return subtype
    return None

################################################################
# These are extension action specific
################################################################

def action_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an action extension
    This is brute force, searching records for a match
    """
    return cls_is_ext_obj(cls, version, extension_action_subtype)

def extension_action_to_subtype(cls, version):
    """
    Return the ID of the action subtype (for its experimenteer)
    if class is an action extension, else None
    """
    if version in extension_action_subtype:
        for exp, classes in extension_action_subtype[version].items():
            if cls in classes:
                return classes[cls]

    return None

################################################################
# These are extension action specific
################################################################

def action_id_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an action ID extension
    This is brute force, searching records for a match
    """
    if version not in [of_g.VERSION_1_3]: # Action IDs only 1.3
        return False
    return cls_is_ext_obj(cls, version, extension_action_id_subtype)

def extension_action_id_to_subtype(cls, version):
    """
    Return the ID of the action ID subtype (for its experimenteer)
    if class is an action ID extension, else None
    """
    if version in extension_action_id_subtype:
        for exp, classes in extension_action_id_subtype[version].items():
            if cls in classes:
                return classes[cls]

    return None

################################################################
# These are extension instruction specific
################################################################

def instruction_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an instruction extension
    This is brute force, searching records for a match
    """
    return cls_is_ext_obj(cls, version, extension_instruction_subtype)

################################################################
# These are extension queue_prop specific
################################################################

def queue_prop_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an instruction extension
    This is brute force, searching records for a match
    """
    return cls_is_ext_obj(cls, version, extension_queue_prop_subtype)

################################################################
# These are extension table_feature_prop specific
################################################################

def table_feature_prop_is_extension(cls, version):
    """
    Return True if cls, version is recognized as an instruction extension
    This is brute force, searching records for a match
    """
    return cls_is_ext_obj(cls, version,
                          extension_table_feature_prop_subtype)
