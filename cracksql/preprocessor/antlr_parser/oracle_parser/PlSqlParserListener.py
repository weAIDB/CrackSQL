# Generated from /data/Coding/LLM4DB/antlr_gram/oracle/PlSqlParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PlSqlParser import PlSqlParser
else:
    from PlSqlParser import PlSqlParser

# This class defines a complete listener for a parse tree produced by PlSqlParser.
class PlSqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by PlSqlParser#sql_script.
    def enterSql_script(self, ctx:PlSqlParser.Sql_scriptContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_script.
    def exitSql_script(self, ctx:PlSqlParser.Sql_scriptContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unit_statement.
    def enterUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unit_statement.
    def exitUnit_statement(self, ctx:PlSqlParser.Unit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_diskgroup.
    def enterAlter_diskgroup(self, ctx:PlSqlParser.Alter_diskgroupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_diskgroup.
    def exitAlter_diskgroup(self, ctx:PlSqlParser.Alter_diskgroupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_disk_clause.
    def enterAdd_disk_clause(self, ctx:PlSqlParser.Add_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_disk_clause.
    def exitAdd_disk_clause(self, ctx:PlSqlParser.Add_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_disk_clause.
    def enterDrop_disk_clause(self, ctx:PlSqlParser.Drop_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_disk_clause.
    def exitDrop_disk_clause(self, ctx:PlSqlParser.Drop_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#resize_disk_clause.
    def enterResize_disk_clause(self, ctx:PlSqlParser.Resize_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#resize_disk_clause.
    def exitResize_disk_clause(self, ctx:PlSqlParser.Resize_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#replace_disk_clause.
    def enterReplace_disk_clause(self, ctx:PlSqlParser.Replace_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#replace_disk_clause.
    def exitReplace_disk_clause(self, ctx:PlSqlParser.Replace_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#wait_nowait.
    def enterWait_nowait(self, ctx:PlSqlParser.Wait_nowaitContext):
        pass

    # Exit a parse tree produced by PlSqlParser#wait_nowait.
    def exitWait_nowait(self, ctx:PlSqlParser.Wait_nowaitContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rename_disk_clause.
    def enterRename_disk_clause(self, ctx:PlSqlParser.Rename_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rename_disk_clause.
    def exitRename_disk_clause(self, ctx:PlSqlParser.Rename_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disk_online_clause.
    def enterDisk_online_clause(self, ctx:PlSqlParser.Disk_online_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disk_online_clause.
    def exitDisk_online_clause(self, ctx:PlSqlParser.Disk_online_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disk_offline_clause.
    def enterDisk_offline_clause(self, ctx:PlSqlParser.Disk_offline_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disk_offline_clause.
    def exitDisk_offline_clause(self, ctx:PlSqlParser.Disk_offline_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#timeout_clause.
    def enterTimeout_clause(self, ctx:PlSqlParser.Timeout_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#timeout_clause.
    def exitTimeout_clause(self, ctx:PlSqlParser.Timeout_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rebalance_diskgroup_clause.
    def enterRebalance_diskgroup_clause(self, ctx:PlSqlParser.Rebalance_diskgroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rebalance_diskgroup_clause.
    def exitRebalance_diskgroup_clause(self, ctx:PlSqlParser.Rebalance_diskgroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#phase.
    def enterPhase(self, ctx:PlSqlParser.PhaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#phase.
    def exitPhase(self, ctx:PlSqlParser.PhaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#check_diskgroup_clause.
    def enterCheck_diskgroup_clause(self, ctx:PlSqlParser.Check_diskgroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#check_diskgroup_clause.
    def exitCheck_diskgroup_clause(self, ctx:PlSqlParser.Check_diskgroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_template_clauses.
    def enterDiskgroup_template_clauses(self, ctx:PlSqlParser.Diskgroup_template_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_template_clauses.
    def exitDiskgroup_template_clauses(self, ctx:PlSqlParser.Diskgroup_template_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#qualified_template_clause.
    def enterQualified_template_clause(self, ctx:PlSqlParser.Qualified_template_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#qualified_template_clause.
    def exitQualified_template_clause(self, ctx:PlSqlParser.Qualified_template_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#redundancy_clause.
    def enterRedundancy_clause(self, ctx:PlSqlParser.Redundancy_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#redundancy_clause.
    def exitRedundancy_clause(self, ctx:PlSqlParser.Redundancy_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#striping_clause.
    def enterStriping_clause(self, ctx:PlSqlParser.Striping_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#striping_clause.
    def exitStriping_clause(self, ctx:PlSqlParser.Striping_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#force_noforce.
    def enterForce_noforce(self, ctx:PlSqlParser.Force_noforceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#force_noforce.
    def exitForce_noforce(self, ctx:PlSqlParser.Force_noforceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_directory_clauses.
    def enterDiskgroup_directory_clauses(self, ctx:PlSqlParser.Diskgroup_directory_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_directory_clauses.
    def exitDiskgroup_directory_clauses(self, ctx:PlSqlParser.Diskgroup_directory_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dir_name.
    def enterDir_name(self, ctx:PlSqlParser.Dir_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dir_name.
    def exitDir_name(self, ctx:PlSqlParser.Dir_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_alias_clauses.
    def enterDiskgroup_alias_clauses(self, ctx:PlSqlParser.Diskgroup_alias_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_alias_clauses.
    def exitDiskgroup_alias_clauses(self, ctx:PlSqlParser.Diskgroup_alias_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_volume_clauses.
    def enterDiskgroup_volume_clauses(self, ctx:PlSqlParser.Diskgroup_volume_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_volume_clauses.
    def exitDiskgroup_volume_clauses(self, ctx:PlSqlParser.Diskgroup_volume_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_volume_clause.
    def enterAdd_volume_clause(self, ctx:PlSqlParser.Add_volume_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_volume_clause.
    def exitAdd_volume_clause(self, ctx:PlSqlParser.Add_volume_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_volume_clause.
    def enterModify_volume_clause(self, ctx:PlSqlParser.Modify_volume_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_volume_clause.
    def exitModify_volume_clause(self, ctx:PlSqlParser.Modify_volume_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_attributes.
    def enterDiskgroup_attributes(self, ctx:PlSqlParser.Diskgroup_attributesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_attributes.
    def exitDiskgroup_attributes(self, ctx:PlSqlParser.Diskgroup_attributesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_diskgroup_file.
    def enterModify_diskgroup_file(self, ctx:PlSqlParser.Modify_diskgroup_fileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_diskgroup_file.
    def exitModify_diskgroup_file(self, ctx:PlSqlParser.Modify_diskgroup_fileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disk_region_clause.
    def enterDisk_region_clause(self, ctx:PlSqlParser.Disk_region_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disk_region_clause.
    def exitDisk_region_clause(self, ctx:PlSqlParser.Disk_region_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_diskgroup_file_clause.
    def enterDrop_diskgroup_file_clause(self, ctx:PlSqlParser.Drop_diskgroup_file_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_diskgroup_file_clause.
    def exitDrop_diskgroup_file_clause(self, ctx:PlSqlParser.Drop_diskgroup_file_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#convert_redundancy_clause.
    def enterConvert_redundancy_clause(self, ctx:PlSqlParser.Convert_redundancy_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#convert_redundancy_clause.
    def exitConvert_redundancy_clause(self, ctx:PlSqlParser.Convert_redundancy_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#usergroup_clauses.
    def enterUsergroup_clauses(self, ctx:PlSqlParser.Usergroup_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#usergroup_clauses.
    def exitUsergroup_clauses(self, ctx:PlSqlParser.Usergroup_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_clauses.
    def enterUser_clauses(self, ctx:PlSqlParser.User_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_clauses.
    def exitUser_clauses(self, ctx:PlSqlParser.User_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#file_permissions_clause.
    def enterFile_permissions_clause(self, ctx:PlSqlParser.File_permissions_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#file_permissions_clause.
    def exitFile_permissions_clause(self, ctx:PlSqlParser.File_permissions_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#file_owner_clause.
    def enterFile_owner_clause(self, ctx:PlSqlParser.File_owner_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#file_owner_clause.
    def exitFile_owner_clause(self, ctx:PlSqlParser.File_owner_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#scrub_clause.
    def enterScrub_clause(self, ctx:PlSqlParser.Scrub_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#scrub_clause.
    def exitScrub_clause(self, ctx:PlSqlParser.Scrub_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quotagroup_clauses.
    def enterQuotagroup_clauses(self, ctx:PlSqlParser.Quotagroup_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quotagroup_clauses.
    def exitQuotagroup_clauses(self, ctx:PlSqlParser.Quotagroup_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#property_name.
    def enterProperty_name(self, ctx:PlSqlParser.Property_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#property_name.
    def exitProperty_name(self, ctx:PlSqlParser.Property_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#property_value.
    def enterProperty_value(self, ctx:PlSqlParser.Property_valueContext):
        pass

    # Exit a parse tree produced by PlSqlParser#property_value.
    def exitProperty_value(self, ctx:PlSqlParser.Property_valueContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filegroup_clauses.
    def enterFilegroup_clauses(self, ctx:PlSqlParser.Filegroup_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filegroup_clauses.
    def exitFilegroup_clauses(self, ctx:PlSqlParser.Filegroup_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_filegroup_clause.
    def enterAdd_filegroup_clause(self, ctx:PlSqlParser.Add_filegroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_filegroup_clause.
    def exitAdd_filegroup_clause(self, ctx:PlSqlParser.Add_filegroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_filegroup_clause.
    def enterModify_filegroup_clause(self, ctx:PlSqlParser.Modify_filegroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_filegroup_clause.
    def exitModify_filegroup_clause(self, ctx:PlSqlParser.Modify_filegroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#move_to_filegroup_clause.
    def enterMove_to_filegroup_clause(self, ctx:PlSqlParser.Move_to_filegroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#move_to_filegroup_clause.
    def exitMove_to_filegroup_clause(self, ctx:PlSqlParser.Move_to_filegroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_filegroup_clause.
    def enterDrop_filegroup_clause(self, ctx:PlSqlParser.Drop_filegroup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_filegroup_clause.
    def exitDrop_filegroup_clause(self, ctx:PlSqlParser.Drop_filegroup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quorum_regular.
    def enterQuorum_regular(self, ctx:PlSqlParser.Quorum_regularContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quorum_regular.
    def exitQuorum_regular(self, ctx:PlSqlParser.Quorum_regularContext):
        pass


    # Enter a parse tree produced by PlSqlParser#undrop_disk_clause.
    def enterUndrop_disk_clause(self, ctx:PlSqlParser.Undrop_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#undrop_disk_clause.
    def exitUndrop_disk_clause(self, ctx:PlSqlParser.Undrop_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#diskgroup_availability.
    def enterDiskgroup_availability(self, ctx:PlSqlParser.Diskgroup_availabilityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#diskgroup_availability.
    def exitDiskgroup_availability(self, ctx:PlSqlParser.Diskgroup_availabilityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#enable_disable_volume.
    def enterEnable_disable_volume(self, ctx:PlSqlParser.Enable_disable_volumeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#enable_disable_volume.
    def exitEnable_disable_volume(self, ctx:PlSqlParser.Enable_disable_volumeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_function.
    def enterDrop_function(self, ctx:PlSqlParser.Drop_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_function.
    def exitDrop_function(self, ctx:PlSqlParser.Drop_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_flashback_archive.
    def enterAlter_flashback_archive(self, ctx:PlSqlParser.Alter_flashback_archiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_flashback_archive.
    def exitAlter_flashback_archive(self, ctx:PlSqlParser.Alter_flashback_archiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_hierarchy.
    def enterAlter_hierarchy(self, ctx:PlSqlParser.Alter_hierarchyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_hierarchy.
    def exitAlter_hierarchy(self, ctx:PlSqlParser.Alter_hierarchyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_function.
    def enterAlter_function(self, ctx:PlSqlParser.Alter_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_function.
    def exitAlter_function(self, ctx:PlSqlParser.Alter_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_java.
    def enterAlter_java(self, ctx:PlSqlParser.Alter_javaContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_java.
    def exitAlter_java(self, ctx:PlSqlParser.Alter_javaContext):
        pass


    # Enter a parse tree produced by PlSqlParser#match_string.
    def enterMatch_string(self, ctx:PlSqlParser.Match_stringContext):
        pass

    # Exit a parse tree produced by PlSqlParser#match_string.
    def exitMatch_string(self, ctx:PlSqlParser.Match_stringContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_function_body.
    def enterCreate_function_body(self, ctx:PlSqlParser.Create_function_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_function_body.
    def exitCreate_function_body(self, ctx:PlSqlParser.Create_function_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_macro_body.
    def enterSql_macro_body(self, ctx:PlSqlParser.Sql_macro_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_macro_body.
    def exitSql_macro_body(self, ctx:PlSqlParser.Sql_macro_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parallel_enable_clause.
    def enterParallel_enable_clause(self, ctx:PlSqlParser.Parallel_enable_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parallel_enable_clause.
    def exitParallel_enable_clause(self, ctx:PlSqlParser.Parallel_enable_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_by_clause.
    def enterPartition_by_clause(self, ctx:PlSqlParser.Partition_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_by_clause.
    def exitPartition_by_clause(self, ctx:PlSqlParser.Partition_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#result_cache_clause.
    def enterResult_cache_clause(self, ctx:PlSqlParser.Result_cache_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#result_cache_clause.
    def exitResult_cache_clause(self, ctx:PlSqlParser.Result_cache_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#accessible_by_clause.
    def enterAccessible_by_clause(self, ctx:PlSqlParser.Accessible_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#accessible_by_clause.
    def exitAccessible_by_clause(self, ctx:PlSqlParser.Accessible_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_collation_clause.
    def enterDefault_collation_clause(self, ctx:PlSqlParser.Default_collation_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_collation_clause.
    def exitDefault_collation_clause(self, ctx:PlSqlParser.Default_collation_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#aggregate_clause.
    def enterAggregate_clause(self, ctx:PlSqlParser.Aggregate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#aggregate_clause.
    def exitAggregate_clause(self, ctx:PlSqlParser.Aggregate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pipelined_using_clause.
    def enterPipelined_using_clause(self, ctx:PlSqlParser.Pipelined_using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pipelined_using_clause.
    def exitPipelined_using_clause(self, ctx:PlSqlParser.Pipelined_using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#accessor.
    def enterAccessor(self, ctx:PlSqlParser.AccessorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#accessor.
    def exitAccessor(self, ctx:PlSqlParser.AccessorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relies_on_part.
    def enterRelies_on_part(self, ctx:PlSqlParser.Relies_on_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relies_on_part.
    def exitRelies_on_part(self, ctx:PlSqlParser.Relies_on_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#streaming_clause.
    def enterStreaming_clause(self, ctx:PlSqlParser.Streaming_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#streaming_clause.
    def exitStreaming_clause(self, ctx:PlSqlParser.Streaming_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_outline.
    def enterAlter_outline(self, ctx:PlSqlParser.Alter_outlineContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_outline.
    def exitAlter_outline(self, ctx:PlSqlParser.Alter_outlineContext):
        pass


    # Enter a parse tree produced by PlSqlParser#outline_options.
    def enterOutline_options(self, ctx:PlSqlParser.Outline_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#outline_options.
    def exitOutline_options(self, ctx:PlSqlParser.Outline_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_lockdown_profile.
    def enterAlter_lockdown_profile(self, ctx:PlSqlParser.Alter_lockdown_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_lockdown_profile.
    def exitAlter_lockdown_profile(self, ctx:PlSqlParser.Alter_lockdown_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lockdown_feature.
    def enterLockdown_feature(self, ctx:PlSqlParser.Lockdown_featureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lockdown_feature.
    def exitLockdown_feature(self, ctx:PlSqlParser.Lockdown_featureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lockdown_options.
    def enterLockdown_options(self, ctx:PlSqlParser.Lockdown_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lockdown_options.
    def exitLockdown_options(self, ctx:PlSqlParser.Lockdown_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lockdown_statements.
    def enterLockdown_statements(self, ctx:PlSqlParser.Lockdown_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lockdown_statements.
    def exitLockdown_statements(self, ctx:PlSqlParser.Lockdown_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#statement_clauses.
    def enterStatement_clauses(self, ctx:PlSqlParser.Statement_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#statement_clauses.
    def exitStatement_clauses(self, ctx:PlSqlParser.Statement_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#clause_options.
    def enterClause_options(self, ctx:PlSqlParser.Clause_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#clause_options.
    def exitClause_options(self, ctx:PlSqlParser.Clause_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#option_values.
    def enterOption_values(self, ctx:PlSqlParser.Option_valuesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#option_values.
    def exitOption_values(self, ctx:PlSqlParser.Option_valuesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#string_list.
    def enterString_list(self, ctx:PlSqlParser.String_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#string_list.
    def exitString_list(self, ctx:PlSqlParser.String_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disable_enable.
    def enterDisable_enable(self, ctx:PlSqlParser.Disable_enableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disable_enable.
    def exitDisable_enable(self, ctx:PlSqlParser.Disable_enableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_lockdown_profile.
    def enterDrop_lockdown_profile(self, ctx:PlSqlParser.Drop_lockdown_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_lockdown_profile.
    def exitDrop_lockdown_profile(self, ctx:PlSqlParser.Drop_lockdown_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_package.
    def enterDrop_package(self, ctx:PlSqlParser.Drop_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_package.
    def exitDrop_package(self, ctx:PlSqlParser.Drop_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_package.
    def enterAlter_package(self, ctx:PlSqlParser.Alter_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_package.
    def exitAlter_package(self, ctx:PlSqlParser.Alter_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_package.
    def enterCreate_package(self, ctx:PlSqlParser.Create_packageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_package.
    def exitCreate_package(self, ctx:PlSqlParser.Create_packageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_package_body.
    def enterCreate_package_body(self, ctx:PlSqlParser.Create_package_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_package_body.
    def exitCreate_package_body(self, ctx:PlSqlParser.Create_package_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_obj_spec.
    def enterPackage_obj_spec(self, ctx:PlSqlParser.Package_obj_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_obj_spec.
    def exitPackage_obj_spec(self, ctx:PlSqlParser.Package_obj_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#procedure_spec.
    def enterProcedure_spec(self, ctx:PlSqlParser.Procedure_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#procedure_spec.
    def exitProcedure_spec(self, ctx:PlSqlParser.Procedure_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_spec.
    def enterFunction_spec(self, ctx:PlSqlParser.Function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_spec.
    def exitFunction_spec(self, ctx:PlSqlParser.Function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_obj_body.
    def enterPackage_obj_body(self, ctx:PlSqlParser.Package_obj_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_obj_body.
    def exitPackage_obj_body(self, ctx:PlSqlParser.Package_obj_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_pmem_filestore.
    def enterAlter_pmem_filestore(self, ctx:PlSqlParser.Alter_pmem_filestoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_pmem_filestore.
    def exitAlter_pmem_filestore(self, ctx:PlSqlParser.Alter_pmem_filestoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_pmem_filestore.
    def enterDrop_pmem_filestore(self, ctx:PlSqlParser.Drop_pmem_filestoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_pmem_filestore.
    def exitDrop_pmem_filestore(self, ctx:PlSqlParser.Drop_pmem_filestoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_procedure.
    def enterDrop_procedure(self, ctx:PlSqlParser.Drop_procedureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_procedure.
    def exitDrop_procedure(self, ctx:PlSqlParser.Drop_procedureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_procedure.
    def enterAlter_procedure(self, ctx:PlSqlParser.Alter_procedureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_procedure.
    def exitAlter_procedure(self, ctx:PlSqlParser.Alter_procedureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_body.
    def enterFunction_body(self, ctx:PlSqlParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_body.
    def exitFunction_body(self, ctx:PlSqlParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#procedure_body.
    def enterProcedure_body(self, ctx:PlSqlParser.Procedure_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#procedure_body.
    def exitProcedure_body(self, ctx:PlSqlParser.Procedure_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_procedure_body.
    def enterCreate_procedure_body(self, ctx:PlSqlParser.Create_procedure_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_procedure_body.
    def exitCreate_procedure_body(self, ctx:PlSqlParser.Create_procedure_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_resource_cost.
    def enterAlter_resource_cost(self, ctx:PlSqlParser.Alter_resource_costContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_resource_cost.
    def exitAlter_resource_cost(self, ctx:PlSqlParser.Alter_resource_costContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_outline.
    def enterDrop_outline(self, ctx:PlSqlParser.Drop_outlineContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_outline.
    def exitDrop_outline(self, ctx:PlSqlParser.Drop_outlineContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_rollback_segment.
    def enterAlter_rollback_segment(self, ctx:PlSqlParser.Alter_rollback_segmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_rollback_segment.
    def exitAlter_rollback_segment(self, ctx:PlSqlParser.Alter_rollback_segmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_restore_point.
    def enterDrop_restore_point(self, ctx:PlSqlParser.Drop_restore_pointContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_restore_point.
    def exitDrop_restore_point(self, ctx:PlSqlParser.Drop_restore_pointContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_rollback_segment.
    def enterDrop_rollback_segment(self, ctx:PlSqlParser.Drop_rollback_segmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_rollback_segment.
    def exitDrop_rollback_segment(self, ctx:PlSqlParser.Drop_rollback_segmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_role.
    def enterDrop_role(self, ctx:PlSqlParser.Drop_roleContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_role.
    def exitDrop_role(self, ctx:PlSqlParser.Drop_roleContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_pmem_filestore.
    def enterCreate_pmem_filestore(self, ctx:PlSqlParser.Create_pmem_filestoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_pmem_filestore.
    def exitCreate_pmem_filestore(self, ctx:PlSqlParser.Create_pmem_filestoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pmem_filestore_options.
    def enterPmem_filestore_options(self, ctx:PlSqlParser.Pmem_filestore_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pmem_filestore_options.
    def exitPmem_filestore_options(self, ctx:PlSqlParser.Pmem_filestore_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#file_path.
    def enterFile_path(self, ctx:PlSqlParser.File_pathContext):
        pass

    # Exit a parse tree produced by PlSqlParser#file_path.
    def exitFile_path(self, ctx:PlSqlParser.File_pathContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_rollback_segment.
    def enterCreate_rollback_segment(self, ctx:PlSqlParser.Create_rollback_segmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_rollback_segment.
    def exitCreate_rollback_segment(self, ctx:PlSqlParser.Create_rollback_segmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_trigger.
    def enterDrop_trigger(self, ctx:PlSqlParser.Drop_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_trigger.
    def exitDrop_trigger(self, ctx:PlSqlParser.Drop_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_trigger.
    def enterAlter_trigger(self, ctx:PlSqlParser.Alter_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_trigger.
    def exitAlter_trigger(self, ctx:PlSqlParser.Alter_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_trigger.
    def enterCreate_trigger(self, ctx:PlSqlParser.Create_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_trigger.
    def exitCreate_trigger(self, ctx:PlSqlParser.Create_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_follows_clause.
    def enterTrigger_follows_clause(self, ctx:PlSqlParser.Trigger_follows_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_follows_clause.
    def exitTrigger_follows_clause(self, ctx:PlSqlParser.Trigger_follows_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_when_clause.
    def enterTrigger_when_clause(self, ctx:PlSqlParser.Trigger_when_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_when_clause.
    def exitTrigger_when_clause(self, ctx:PlSqlParser.Trigger_when_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_dml_trigger.
    def enterSimple_dml_trigger(self, ctx:PlSqlParser.Simple_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_dml_trigger.
    def exitSimple_dml_trigger(self, ctx:PlSqlParser.Simple_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_each_row.
    def enterFor_each_row(self, ctx:PlSqlParser.For_each_rowContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_each_row.
    def exitFor_each_row(self, ctx:PlSqlParser.For_each_rowContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compound_dml_trigger.
    def enterCompound_dml_trigger(self, ctx:PlSqlParser.Compound_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compound_dml_trigger.
    def exitCompound_dml_trigger(self, ctx:PlSqlParser.Compound_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_dml_trigger.
    def enterNon_dml_trigger(self, ctx:PlSqlParser.Non_dml_triggerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_dml_trigger.
    def exitNon_dml_trigger(self, ctx:PlSqlParser.Non_dml_triggerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_body.
    def enterTrigger_body(self, ctx:PlSqlParser.Trigger_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_body.
    def exitTrigger_body(self, ctx:PlSqlParser.Trigger_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#routine_clause.
    def enterRoutine_clause(self, ctx:PlSqlParser.Routine_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#routine_clause.
    def exitRoutine_clause(self, ctx:PlSqlParser.Routine_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compound_trigger_block.
    def enterCompound_trigger_block(self, ctx:PlSqlParser.Compound_trigger_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compound_trigger_block.
    def exitCompound_trigger_block(self, ctx:PlSqlParser.Compound_trigger_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#timing_point_section.
    def enterTiming_point_section(self, ctx:PlSqlParser.Timing_point_sectionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#timing_point_section.
    def exitTiming_point_section(self, ctx:PlSqlParser.Timing_point_sectionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_dml_event.
    def enterNon_dml_event(self, ctx:PlSqlParser.Non_dml_eventContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_dml_event.
    def exitNon_dml_event(self, ctx:PlSqlParser.Non_dml_eventContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_clause.
    def enterDml_event_clause(self, ctx:PlSqlParser.Dml_event_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_clause.
    def exitDml_event_clause(self, ctx:PlSqlParser.Dml_event_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_element.
    def enterDml_event_element(self, ctx:PlSqlParser.Dml_event_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_element.
    def exitDml_event_element(self, ctx:PlSqlParser.Dml_event_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_event_nested_clause.
    def enterDml_event_nested_clause(self, ctx:PlSqlParser.Dml_event_nested_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_event_nested_clause.
    def exitDml_event_nested_clause(self, ctx:PlSqlParser.Dml_event_nested_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#referencing_clause.
    def enterReferencing_clause(self, ctx:PlSqlParser.Referencing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#referencing_clause.
    def exitReferencing_clause(self, ctx:PlSqlParser.Referencing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#referencing_element.
    def enterReferencing_element(self, ctx:PlSqlParser.Referencing_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#referencing_element.
    def exitReferencing_element(self, ctx:PlSqlParser.Referencing_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_type.
    def enterDrop_type(self, ctx:PlSqlParser.Drop_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_type.
    def exitDrop_type(self, ctx:PlSqlParser.Drop_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_type.
    def enterAlter_type(self, ctx:PlSqlParser.Alter_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_type.
    def exitAlter_type(self, ctx:PlSqlParser.Alter_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compile_type_clause.
    def enterCompile_type_clause(self, ctx:PlSqlParser.Compile_type_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compile_type_clause.
    def exitCompile_type_clause(self, ctx:PlSqlParser.Compile_type_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#replace_type_clause.
    def enterReplace_type_clause(self, ctx:PlSqlParser.Replace_type_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#replace_type_clause.
    def exitReplace_type_clause(self, ctx:PlSqlParser.Replace_type_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_method_spec.
    def enterAlter_method_spec(self, ctx:PlSqlParser.Alter_method_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_method_spec.
    def exitAlter_method_spec(self, ctx:PlSqlParser.Alter_method_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_method_element.
    def enterAlter_method_element(self, ctx:PlSqlParser.Alter_method_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_method_element.
    def exitAlter_method_element(self, ctx:PlSqlParser.Alter_method_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_attribute_definition.
    def enterAlter_attribute_definition(self, ctx:PlSqlParser.Alter_attribute_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_attribute_definition.
    def exitAlter_attribute_definition(self, ctx:PlSqlParser.Alter_attribute_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_definition.
    def enterAttribute_definition(self, ctx:PlSqlParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_definition.
    def exitAttribute_definition(self, ctx:PlSqlParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_collection_clauses.
    def enterAlter_collection_clauses(self, ctx:PlSqlParser.Alter_collection_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_collection_clauses.
    def exitAlter_collection_clauses(self, ctx:PlSqlParser.Alter_collection_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dependent_handling_clause.
    def enterDependent_handling_clause(self, ctx:PlSqlParser.Dependent_handling_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dependent_handling_clause.
    def exitDependent_handling_clause(self, ctx:PlSqlParser.Dependent_handling_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dependent_exceptions_part.
    def enterDependent_exceptions_part(self, ctx:PlSqlParser.Dependent_exceptions_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dependent_exceptions_part.
    def exitDependent_exceptions_part(self, ctx:PlSqlParser.Dependent_exceptions_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_type.
    def enterCreate_type(self, ctx:PlSqlParser.Create_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_type.
    def exitCreate_type(self, ctx:PlSqlParser.Create_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_definition.
    def enterType_definition(self, ctx:PlSqlParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_definition.
    def exitType_definition(self, ctx:PlSqlParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_type_def.
    def enterObject_type_def(self, ctx:PlSqlParser.Object_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_type_def.
    def exitObject_type_def(self, ctx:PlSqlParser.Object_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_as_part.
    def enterObject_as_part(self, ctx:PlSqlParser.Object_as_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_as_part.
    def exitObject_as_part(self, ctx:PlSqlParser.Object_as_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_under_part.
    def enterObject_under_part(self, ctx:PlSqlParser.Object_under_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_under_part.
    def exitObject_under_part(self, ctx:PlSqlParser.Object_under_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#nested_table_type_def.
    def enterNested_table_type_def(self, ctx:PlSqlParser.Nested_table_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#nested_table_type_def.
    def exitNested_table_type_def(self, ctx:PlSqlParser.Nested_table_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sqlj_object_type.
    def enterSqlj_object_type(self, ctx:PlSqlParser.Sqlj_object_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sqlj_object_type.
    def exitSqlj_object_type(self, ctx:PlSqlParser.Sqlj_object_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_body.
    def enterType_body(self, ctx:PlSqlParser.Type_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_body.
    def exitType_body(self, ctx:PlSqlParser.Type_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_body_elements.
    def enterType_body_elements(self, ctx:PlSqlParser.Type_body_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_body_elements.
    def exitType_body_elements(self, ctx:PlSqlParser.Type_body_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#map_order_func_declaration.
    def enterMap_order_func_declaration(self, ctx:PlSqlParser.Map_order_func_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#map_order_func_declaration.
    def exitMap_order_func_declaration(self, ctx:PlSqlParser.Map_order_func_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subprog_decl_in_type.
    def enterSubprog_decl_in_type(self, ctx:PlSqlParser.Subprog_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subprog_decl_in_type.
    def exitSubprog_decl_in_type(self, ctx:PlSqlParser.Subprog_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#proc_decl_in_type.
    def enterProc_decl_in_type(self, ctx:PlSqlParser.Proc_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#proc_decl_in_type.
    def exitProc_decl_in_type(self, ctx:PlSqlParser.Proc_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#func_decl_in_type.
    def enterFunc_decl_in_type(self, ctx:PlSqlParser.Func_decl_in_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#func_decl_in_type.
    def exitFunc_decl_in_type(self, ctx:PlSqlParser.Func_decl_in_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:PlSqlParser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:PlSqlParser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modifier_clause.
    def enterModifier_clause(self, ctx:PlSqlParser.Modifier_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modifier_clause.
    def exitModifier_clause(self, ctx:PlSqlParser.Modifier_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_member_spec.
    def enterObject_member_spec(self, ctx:PlSqlParser.Object_member_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_member_spec.
    def exitObject_member_spec(self, ctx:PlSqlParser.Object_member_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sqlj_object_type_attr.
    def enterSqlj_object_type_attr(self, ctx:PlSqlParser.Sqlj_object_type_attrContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sqlj_object_type_attr.
    def exitSqlj_object_type_attr(self, ctx:PlSqlParser.Sqlj_object_type_attrContext):
        pass


    # Enter a parse tree produced by PlSqlParser#element_spec.
    def enterElement_spec(self, ctx:PlSqlParser.Element_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#element_spec.
    def exitElement_spec(self, ctx:PlSqlParser.Element_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#element_spec_options.
    def enterElement_spec_options(self, ctx:PlSqlParser.Element_spec_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#element_spec_options.
    def exitElement_spec_options(self, ctx:PlSqlParser.Element_spec_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subprogram_spec.
    def enterSubprogram_spec(self, ctx:PlSqlParser.Subprogram_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subprogram_spec.
    def exitSubprogram_spec(self, ctx:PlSqlParser.Subprogram_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#overriding_subprogram_spec.
    def enterOverriding_subprogram_spec(self, ctx:PlSqlParser.Overriding_subprogram_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#overriding_subprogram_spec.
    def exitOverriding_subprogram_spec(self, ctx:PlSqlParser.Overriding_subprogram_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#overriding_function_spec.
    def enterOverriding_function_spec(self, ctx:PlSqlParser.Overriding_function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#overriding_function_spec.
    def exitOverriding_function_spec(self, ctx:PlSqlParser.Overriding_function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_procedure_spec.
    def enterType_procedure_spec(self, ctx:PlSqlParser.Type_procedure_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_procedure_spec.
    def exitType_procedure_spec(self, ctx:PlSqlParser.Type_procedure_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_function_spec.
    def enterType_function_spec(self, ctx:PlSqlParser.Type_function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_function_spec.
    def exitType_function_spec(self, ctx:PlSqlParser.Type_function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constructor_spec.
    def enterConstructor_spec(self, ctx:PlSqlParser.Constructor_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constructor_spec.
    def exitConstructor_spec(self, ctx:PlSqlParser.Constructor_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#map_order_function_spec.
    def enterMap_order_function_spec(self, ctx:PlSqlParser.Map_order_function_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#map_order_function_spec.
    def exitMap_order_function_spec(self, ctx:PlSqlParser.Map_order_function_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_clause.
    def enterPragma_clause(self, ctx:PlSqlParser.Pragma_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_clause.
    def exitPragma_clause(self, ctx:PlSqlParser.Pragma_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_elements.
    def enterPragma_elements(self, ctx:PlSqlParser.Pragma_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_elements.
    def exitPragma_elements(self, ctx:PlSqlParser.Pragma_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_elements_parameter.
    def enterType_elements_parameter(self, ctx:PlSqlParser.Type_elements_parameterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_elements_parameter.
    def exitType_elements_parameter(self, ctx:PlSqlParser.Type_elements_parameterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_sequence.
    def enterDrop_sequence(self, ctx:PlSqlParser.Drop_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_sequence.
    def exitDrop_sequence(self, ctx:PlSqlParser.Drop_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_sequence.
    def enterAlter_sequence(self, ctx:PlSqlParser.Alter_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_sequence.
    def exitAlter_sequence(self, ctx:PlSqlParser.Alter_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_session.
    def enterAlter_session(self, ctx:PlSqlParser.Alter_sessionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_session.
    def exitAlter_session(self, ctx:PlSqlParser.Alter_sessionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_session_set_clause.
    def enterAlter_session_set_clause(self, ctx:PlSqlParser.Alter_session_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_session_set_clause.
    def exitAlter_session_set_clause(self, ctx:PlSqlParser.Alter_session_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_sequence.
    def enterCreate_sequence(self, ctx:PlSqlParser.Create_sequenceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_sequence.
    def exitCreate_sequence(self, ctx:PlSqlParser.Create_sequenceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_spec.
    def enterSequence_spec(self, ctx:PlSqlParser.Sequence_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_spec.
    def exitSequence_spec(self, ctx:PlSqlParser.Sequence_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_start_clause.
    def enterSequence_start_clause(self, ctx:PlSqlParser.Sequence_start_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_start_clause.
    def exitSequence_start_clause(self, ctx:PlSqlParser.Sequence_start_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_analytic_view.
    def enterCreate_analytic_view(self, ctx:PlSqlParser.Create_analytic_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_analytic_view.
    def exitCreate_analytic_view(self, ctx:PlSqlParser.Create_analytic_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#classification_clause.
    def enterClassification_clause(self, ctx:PlSqlParser.Classification_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#classification_clause.
    def exitClassification_clause(self, ctx:PlSqlParser.Classification_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#caption_clause.
    def enterCaption_clause(self, ctx:PlSqlParser.Caption_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#caption_clause.
    def exitCaption_clause(self, ctx:PlSqlParser.Caption_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#description_clause.
    def enterDescription_clause(self, ctx:PlSqlParser.Description_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#description_clause.
    def exitDescription_clause(self, ctx:PlSqlParser.Description_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#classification_item.
    def enterClassification_item(self, ctx:PlSqlParser.Classification_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#classification_item.
    def exitClassification_item(self, ctx:PlSqlParser.Classification_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#language.
    def enterLanguage(self, ctx:PlSqlParser.LanguageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#language.
    def exitLanguage(self, ctx:PlSqlParser.LanguageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cav_using_clause.
    def enterCav_using_clause(self, ctx:PlSqlParser.Cav_using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cav_using_clause.
    def exitCav_using_clause(self, ctx:PlSqlParser.Cav_using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dim_by_clause.
    def enterDim_by_clause(self, ctx:PlSqlParser.Dim_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dim_by_clause.
    def exitDim_by_clause(self, ctx:PlSqlParser.Dim_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dim_key.
    def enterDim_key(self, ctx:PlSqlParser.Dim_keyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dim_key.
    def exitDim_key(self, ctx:PlSqlParser.Dim_keyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dim_ref.
    def enterDim_ref(self, ctx:PlSqlParser.Dim_refContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dim_ref.
    def exitDim_ref(self, ctx:PlSqlParser.Dim_refContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hier_ref.
    def enterHier_ref(self, ctx:PlSqlParser.Hier_refContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hier_ref.
    def exitHier_ref(self, ctx:PlSqlParser.Hier_refContext):
        pass


    # Enter a parse tree produced by PlSqlParser#measures_clause.
    def enterMeasures_clause(self, ctx:PlSqlParser.Measures_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#measures_clause.
    def exitMeasures_clause(self, ctx:PlSqlParser.Measures_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#av_measure.
    def enterAv_measure(self, ctx:PlSqlParser.Av_measureContext):
        pass

    # Exit a parse tree produced by PlSqlParser#av_measure.
    def exitAv_measure(self, ctx:PlSqlParser.Av_measureContext):
        pass


    # Enter a parse tree produced by PlSqlParser#base_meas_clause.
    def enterBase_meas_clause(self, ctx:PlSqlParser.Base_meas_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#base_meas_clause.
    def exitBase_meas_clause(self, ctx:PlSqlParser.Base_meas_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#meas_aggregate_clause.
    def enterMeas_aggregate_clause(self, ctx:PlSqlParser.Meas_aggregate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#meas_aggregate_clause.
    def exitMeas_aggregate_clause(self, ctx:PlSqlParser.Meas_aggregate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#calc_meas_clause.
    def enterCalc_meas_clause(self, ctx:PlSqlParser.Calc_meas_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#calc_meas_clause.
    def exitCalc_meas_clause(self, ctx:PlSqlParser.Calc_meas_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_measure_clause.
    def enterDefault_measure_clause(self, ctx:PlSqlParser.Default_measure_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_measure_clause.
    def exitDefault_measure_clause(self, ctx:PlSqlParser.Default_measure_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_aggregate_clause.
    def enterDefault_aggregate_clause(self, ctx:PlSqlParser.Default_aggregate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_aggregate_clause.
    def exitDefault_aggregate_clause(self, ctx:PlSqlParser.Default_aggregate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cache_clause.
    def enterCache_clause(self, ctx:PlSqlParser.Cache_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cache_clause.
    def exitCache_clause(self, ctx:PlSqlParser.Cache_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cache_specification.
    def enterCache_specification(self, ctx:PlSqlParser.Cache_specificationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cache_specification.
    def exitCache_specification(self, ctx:PlSqlParser.Cache_specificationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#levels_clause.
    def enterLevels_clause(self, ctx:PlSqlParser.Levels_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#levels_clause.
    def exitLevels_clause(self, ctx:PlSqlParser.Levels_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#level_specification.
    def enterLevel_specification(self, ctx:PlSqlParser.Level_specificationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#level_specification.
    def exitLevel_specification(self, ctx:PlSqlParser.Level_specificationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#level_group_type.
    def enterLevel_group_type(self, ctx:PlSqlParser.Level_group_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#level_group_type.
    def exitLevel_group_type(self, ctx:PlSqlParser.Level_group_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#fact_columns_clause.
    def enterFact_columns_clause(self, ctx:PlSqlParser.Fact_columns_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#fact_columns_clause.
    def exitFact_columns_clause(self, ctx:PlSqlParser.Fact_columns_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#qry_transform_clause.
    def enterQry_transform_clause(self, ctx:PlSqlParser.Qry_transform_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#qry_transform_clause.
    def exitQry_transform_clause(self, ctx:PlSqlParser.Qry_transform_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_attribute_dimension.
    def enterCreate_attribute_dimension(self, ctx:PlSqlParser.Create_attribute_dimensionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_attribute_dimension.
    def exitCreate_attribute_dimension(self, ctx:PlSqlParser.Create_attribute_dimensionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ad_using_clause.
    def enterAd_using_clause(self, ctx:PlSqlParser.Ad_using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ad_using_clause.
    def exitAd_using_clause(self, ctx:PlSqlParser.Ad_using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#source_clause.
    def enterSource_clause(self, ctx:PlSqlParser.Source_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#source_clause.
    def exitSource_clause(self, ctx:PlSqlParser.Source_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_path_clause.
    def enterJoin_path_clause(self, ctx:PlSqlParser.Join_path_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_path_clause.
    def exitJoin_path_clause(self, ctx:PlSqlParser.Join_path_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_condition.
    def enterJoin_condition(self, ctx:PlSqlParser.Join_conditionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_condition.
    def exitJoin_condition(self, ctx:PlSqlParser.Join_conditionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_condition_item.
    def enterJoin_condition_item(self, ctx:PlSqlParser.Join_condition_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_condition_item.
    def exitJoin_condition_item(self, ctx:PlSqlParser.Join_condition_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attributes_clause.
    def enterAttributes_clause(self, ctx:PlSqlParser.Attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attributes_clause.
    def exitAttributes_clause(self, ctx:PlSqlParser.Attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ad_attributes_clause.
    def enterAd_attributes_clause(self, ctx:PlSqlParser.Ad_attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ad_attributes_clause.
    def exitAd_attributes_clause(self, ctx:PlSqlParser.Ad_attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ad_level_clause.
    def enterAd_level_clause(self, ctx:PlSqlParser.Ad_level_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ad_level_clause.
    def exitAd_level_clause(self, ctx:PlSqlParser.Ad_level_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#key_clause.
    def enterKey_clause(self, ctx:PlSqlParser.Key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#key_clause.
    def exitKey_clause(self, ctx:PlSqlParser.Key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alternate_key_clause.
    def enterAlternate_key_clause(self, ctx:PlSqlParser.Alternate_key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alternate_key_clause.
    def exitAlternate_key_clause(self, ctx:PlSqlParser.Alternate_key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dim_order_clause.
    def enterDim_order_clause(self, ctx:PlSqlParser.Dim_order_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dim_order_clause.
    def exitDim_order_clause(self, ctx:PlSqlParser.Dim_order_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#all_clause.
    def enterAll_clause(self, ctx:PlSqlParser.All_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#all_clause.
    def exitAll_clause(self, ctx:PlSqlParser.All_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_audit_policy.
    def enterCreate_audit_policy(self, ctx:PlSqlParser.Create_audit_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_audit_policy.
    def exitCreate_audit_policy(self, ctx:PlSqlParser.Create_audit_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#privilege_audit_clause.
    def enterPrivilege_audit_clause(self, ctx:PlSqlParser.Privilege_audit_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#privilege_audit_clause.
    def exitPrivilege_audit_clause(self, ctx:PlSqlParser.Privilege_audit_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#action_audit_clause.
    def enterAction_audit_clause(self, ctx:PlSqlParser.Action_audit_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#action_audit_clause.
    def exitAction_audit_clause(self, ctx:PlSqlParser.Action_audit_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#system_actions.
    def enterSystem_actions(self, ctx:PlSqlParser.System_actionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#system_actions.
    def exitSystem_actions(self, ctx:PlSqlParser.System_actionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#standard_actions.
    def enterStandard_actions(self, ctx:PlSqlParser.Standard_actionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#standard_actions.
    def exitStandard_actions(self, ctx:PlSqlParser.Standard_actionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#actions_clause.
    def enterActions_clause(self, ctx:PlSqlParser.Actions_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#actions_clause.
    def exitActions_clause(self, ctx:PlSqlParser.Actions_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_action.
    def enterObject_action(self, ctx:PlSqlParser.Object_actionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_action.
    def exitObject_action(self, ctx:PlSqlParser.Object_actionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#system_action.
    def enterSystem_action(self, ctx:PlSqlParser.System_actionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#system_action.
    def exitSystem_action(self, ctx:PlSqlParser.System_actionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#component_actions.
    def enterComponent_actions(self, ctx:PlSqlParser.Component_actionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#component_actions.
    def exitComponent_actions(self, ctx:PlSqlParser.Component_actionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#component_action.
    def enterComponent_action(self, ctx:PlSqlParser.Component_actionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#component_action.
    def exitComponent_action(self, ctx:PlSqlParser.Component_actionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#role_audit_clause.
    def enterRole_audit_clause(self, ctx:PlSqlParser.Role_audit_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#role_audit_clause.
    def exitRole_audit_clause(self, ctx:PlSqlParser.Role_audit_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_controlfile.
    def enterCreate_controlfile(self, ctx:PlSqlParser.Create_controlfileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_controlfile.
    def exitCreate_controlfile(self, ctx:PlSqlParser.Create_controlfileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#controlfile_options.
    def enterControlfile_options(self, ctx:PlSqlParser.Controlfile_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#controlfile_options.
    def exitControlfile_options(self, ctx:PlSqlParser.Controlfile_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logfile_clause.
    def enterLogfile_clause(self, ctx:PlSqlParser.Logfile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logfile_clause.
    def exitLogfile_clause(self, ctx:PlSqlParser.Logfile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#character_set_clause.
    def enterCharacter_set_clause(self, ctx:PlSqlParser.Character_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#character_set_clause.
    def exitCharacter_set_clause(self, ctx:PlSqlParser.Character_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#file_specification.
    def enterFile_specification(self, ctx:PlSqlParser.File_specificationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#file_specification.
    def exitFile_specification(self, ctx:PlSqlParser.File_specificationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_diskgroup.
    def enterCreate_diskgroup(self, ctx:PlSqlParser.Create_diskgroupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_diskgroup.
    def exitCreate_diskgroup(self, ctx:PlSqlParser.Create_diskgroupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#qualified_disk_clause.
    def enterQualified_disk_clause(self, ctx:PlSqlParser.Qualified_disk_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#qualified_disk_clause.
    def exitQualified_disk_clause(self, ctx:PlSqlParser.Qualified_disk_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_edition.
    def enterCreate_edition(self, ctx:PlSqlParser.Create_editionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_edition.
    def exitCreate_edition(self, ctx:PlSqlParser.Create_editionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_flashback_archive.
    def enterCreate_flashback_archive(self, ctx:PlSqlParser.Create_flashback_archiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_flashback_archive.
    def exitCreate_flashback_archive(self, ctx:PlSqlParser.Create_flashback_archiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_archive_quota.
    def enterFlashback_archive_quota(self, ctx:PlSqlParser.Flashback_archive_quotaContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_archive_quota.
    def exitFlashback_archive_quota(self, ctx:PlSqlParser.Flashback_archive_quotaContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_archive_retention.
    def enterFlashback_archive_retention(self, ctx:PlSqlParser.Flashback_archive_retentionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_archive_retention.
    def exitFlashback_archive_retention(self, ctx:PlSqlParser.Flashback_archive_retentionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_hierarchy.
    def enterCreate_hierarchy(self, ctx:PlSqlParser.Create_hierarchyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_hierarchy.
    def exitCreate_hierarchy(self, ctx:PlSqlParser.Create_hierarchyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hier_using_clause.
    def enterHier_using_clause(self, ctx:PlSqlParser.Hier_using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hier_using_clause.
    def exitHier_using_clause(self, ctx:PlSqlParser.Hier_using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#level_hier_clause.
    def enterLevel_hier_clause(self, ctx:PlSqlParser.Level_hier_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#level_hier_clause.
    def exitLevel_hier_clause(self, ctx:PlSqlParser.Level_hier_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hier_attrs_clause.
    def enterHier_attrs_clause(self, ctx:PlSqlParser.Hier_attrs_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hier_attrs_clause.
    def exitHier_attrs_clause(self, ctx:PlSqlParser.Hier_attrs_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hier_attr_clause.
    def enterHier_attr_clause(self, ctx:PlSqlParser.Hier_attr_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hier_attr_clause.
    def exitHier_attr_clause(self, ctx:PlSqlParser.Hier_attr_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hier_attr_name.
    def enterHier_attr_name(self, ctx:PlSqlParser.Hier_attr_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hier_attr_name.
    def exitHier_attr_name(self, ctx:PlSqlParser.Hier_attr_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_index.
    def enterCreate_index(self, ctx:PlSqlParser.Create_indexContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_index.
    def exitCreate_index(self, ctx:PlSqlParser.Create_indexContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cluster_index_clause.
    def enterCluster_index_clause(self, ctx:PlSqlParser.Cluster_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cluster_index_clause.
    def exitCluster_index_clause(self, ctx:PlSqlParser.Cluster_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cluster_name.
    def enterCluster_name(self, ctx:PlSqlParser.Cluster_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cluster_name.
    def exitCluster_name(self, ctx:PlSqlParser.Cluster_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_index_clause.
    def enterTable_index_clause(self, ctx:PlSqlParser.Table_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_index_clause.
    def exitTable_index_clause(self, ctx:PlSqlParser.Table_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#bitmap_join_index_clause.
    def enterBitmap_join_index_clause(self, ctx:PlSqlParser.Bitmap_join_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#bitmap_join_index_clause.
    def exitBitmap_join_index_clause(self, ctx:PlSqlParser.Bitmap_join_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_expr.
    def enterIndex_expr(self, ctx:PlSqlParser.Index_exprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_expr.
    def exitIndex_expr(self, ctx:PlSqlParser.Index_exprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_properties.
    def enterIndex_properties(self, ctx:PlSqlParser.Index_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_properties.
    def exitIndex_properties(self, ctx:PlSqlParser.Index_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#domain_index_clause.
    def enterDomain_index_clause(self, ctx:PlSqlParser.Domain_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#domain_index_clause.
    def exitDomain_index_clause(self, ctx:PlSqlParser.Domain_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#local_domain_index_clause.
    def enterLocal_domain_index_clause(self, ctx:PlSqlParser.Local_domain_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#local_domain_index_clause.
    def exitLocal_domain_index_clause(self, ctx:PlSqlParser.Local_domain_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlindex_clause.
    def enterXmlindex_clause(self, ctx:PlSqlParser.Xmlindex_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlindex_clause.
    def exitXmlindex_clause(self, ctx:PlSqlParser.Xmlindex_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#local_xmlindex_clause.
    def enterLocal_xmlindex_clause(self, ctx:PlSqlParser.Local_xmlindex_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#local_xmlindex_clause.
    def exitLocal_xmlindex_clause(self, ctx:PlSqlParser.Local_xmlindex_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#global_partitioned_index.
    def enterGlobal_partitioned_index(self, ctx:PlSqlParser.Global_partitioned_indexContext):
        pass

    # Exit a parse tree produced by PlSqlParser#global_partitioned_index.
    def exitGlobal_partitioned_index(self, ctx:PlSqlParser.Global_partitioned_indexContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_partitioning_clause.
    def enterIndex_partitioning_clause(self, ctx:PlSqlParser.Index_partitioning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_partitioning_clause.
    def exitIndex_partitioning_clause(self, ctx:PlSqlParser.Index_partitioning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_partitioning_values_list.
    def enterIndex_partitioning_values_list(self, ctx:PlSqlParser.Index_partitioning_values_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_partitioning_values_list.
    def exitIndex_partitioning_values_list(self, ctx:PlSqlParser.Index_partitioning_values_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#local_partitioned_index.
    def enterLocal_partitioned_index(self, ctx:PlSqlParser.Local_partitioned_indexContext):
        pass

    # Exit a parse tree produced by PlSqlParser#local_partitioned_index.
    def exitLocal_partitioned_index(self, ctx:PlSqlParser.Local_partitioned_indexContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_range_partitioned_table.
    def enterOn_range_partitioned_table(self, ctx:PlSqlParser.On_range_partitioned_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_range_partitioned_table.
    def exitOn_range_partitioned_table(self, ctx:PlSqlParser.On_range_partitioned_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_list_partitioned_table.
    def enterOn_list_partitioned_table(self, ctx:PlSqlParser.On_list_partitioned_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_list_partitioned_table.
    def exitOn_list_partitioned_table(self, ctx:PlSqlParser.On_list_partitioned_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partitioned_table.
    def enterPartitioned_table(self, ctx:PlSqlParser.Partitioned_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partitioned_table.
    def exitPartitioned_table(self, ctx:PlSqlParser.Partitioned_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_hash_partitioned_table.
    def enterOn_hash_partitioned_table(self, ctx:PlSqlParser.On_hash_partitioned_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_hash_partitioned_table.
    def exitOn_hash_partitioned_table(self, ctx:PlSqlParser.On_hash_partitioned_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_hash_partitioned_clause.
    def enterOn_hash_partitioned_clause(self, ctx:PlSqlParser.On_hash_partitioned_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_hash_partitioned_clause.
    def exitOn_hash_partitioned_clause(self, ctx:PlSqlParser.On_hash_partitioned_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_comp_partitioned_table.
    def enterOn_comp_partitioned_table(self, ctx:PlSqlParser.On_comp_partitioned_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_comp_partitioned_table.
    def exitOn_comp_partitioned_table(self, ctx:PlSqlParser.On_comp_partitioned_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_comp_partitioned_clause.
    def enterOn_comp_partitioned_clause(self, ctx:PlSqlParser.On_comp_partitioned_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_comp_partitioned_clause.
    def exitOn_comp_partitioned_clause(self, ctx:PlSqlParser.On_comp_partitioned_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_subpartition_clause.
    def enterIndex_subpartition_clause(self, ctx:PlSqlParser.Index_subpartition_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_subpartition_clause.
    def exitIndex_subpartition_clause(self, ctx:PlSqlParser.Index_subpartition_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_subpartition_subclause.
    def enterIndex_subpartition_subclause(self, ctx:PlSqlParser.Index_subpartition_subclauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_subpartition_subclause.
    def exitIndex_subpartition_subclause(self, ctx:PlSqlParser.Index_subpartition_subclauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#odci_parameters.
    def enterOdci_parameters(self, ctx:PlSqlParser.Odci_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#odci_parameters.
    def exitOdci_parameters(self, ctx:PlSqlParser.Odci_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#indextype.
    def enterIndextype(self, ctx:PlSqlParser.IndextypeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#indextype.
    def exitIndextype(self, ctx:PlSqlParser.IndextypeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_index.
    def enterAlter_index(self, ctx:PlSqlParser.Alter_indexContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_index.
    def exitAlter_index(self, ctx:PlSqlParser.Alter_indexContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_index_ops_set1.
    def enterAlter_index_ops_set1(self, ctx:PlSqlParser.Alter_index_ops_set1Context):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_index_ops_set1.
    def exitAlter_index_ops_set1(self, ctx:PlSqlParser.Alter_index_ops_set1Context):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_index_ops_set2.
    def enterAlter_index_ops_set2(self, ctx:PlSqlParser.Alter_index_ops_set2Context):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_index_ops_set2.
    def exitAlter_index_ops_set2(self, ctx:PlSqlParser.Alter_index_ops_set2Context):
        pass


    # Enter a parse tree produced by PlSqlParser#visible_or_invisible.
    def enterVisible_or_invisible(self, ctx:PlSqlParser.Visible_or_invisibleContext):
        pass

    # Exit a parse tree produced by PlSqlParser#visible_or_invisible.
    def exitVisible_or_invisible(self, ctx:PlSqlParser.Visible_or_invisibleContext):
        pass


    # Enter a parse tree produced by PlSqlParser#monitoring_nomonitoring.
    def enterMonitoring_nomonitoring(self, ctx:PlSqlParser.Monitoring_nomonitoringContext):
        pass

    # Exit a parse tree produced by PlSqlParser#monitoring_nomonitoring.
    def exitMonitoring_nomonitoring(self, ctx:PlSqlParser.Monitoring_nomonitoringContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rebuild_clause.
    def enterRebuild_clause(self, ctx:PlSqlParser.Rebuild_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rebuild_clause.
    def exitRebuild_clause(self, ctx:PlSqlParser.Rebuild_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_index_partitioning.
    def enterAlter_index_partitioning(self, ctx:PlSqlParser.Alter_index_partitioningContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_index_partitioning.
    def exitAlter_index_partitioning(self, ctx:PlSqlParser.Alter_index_partitioningContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_index_default_attrs.
    def enterModify_index_default_attrs(self, ctx:PlSqlParser.Modify_index_default_attrsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_index_default_attrs.
    def exitModify_index_default_attrs(self, ctx:PlSqlParser.Modify_index_default_attrsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_hash_index_partition.
    def enterAdd_hash_index_partition(self, ctx:PlSqlParser.Add_hash_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_hash_index_partition.
    def exitAdd_hash_index_partition(self, ctx:PlSqlParser.Add_hash_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#coalesce_index_partition.
    def enterCoalesce_index_partition(self, ctx:PlSqlParser.Coalesce_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#coalesce_index_partition.
    def exitCoalesce_index_partition(self, ctx:PlSqlParser.Coalesce_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_index_partition.
    def enterModify_index_partition(self, ctx:PlSqlParser.Modify_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_index_partition.
    def exitModify_index_partition(self, ctx:PlSqlParser.Modify_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_index_partitions_ops.
    def enterModify_index_partitions_ops(self, ctx:PlSqlParser.Modify_index_partitions_opsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_index_partitions_ops.
    def exitModify_index_partitions_ops(self, ctx:PlSqlParser.Modify_index_partitions_opsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rename_index_partition.
    def enterRename_index_partition(self, ctx:PlSqlParser.Rename_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rename_index_partition.
    def exitRename_index_partition(self, ctx:PlSqlParser.Rename_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_index_partition.
    def enterDrop_index_partition(self, ctx:PlSqlParser.Drop_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_index_partition.
    def exitDrop_index_partition(self, ctx:PlSqlParser.Drop_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#split_index_partition.
    def enterSplit_index_partition(self, ctx:PlSqlParser.Split_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#split_index_partition.
    def exitSplit_index_partition(self, ctx:PlSqlParser.Split_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_partition_description.
    def enterIndex_partition_description(self, ctx:PlSqlParser.Index_partition_descriptionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_partition_description.
    def exitIndex_partition_description(self, ctx:PlSqlParser.Index_partition_descriptionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_index_subpartition.
    def enterModify_index_subpartition(self, ctx:PlSqlParser.Modify_index_subpartitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_index_subpartition.
    def exitModify_index_subpartition(self, ctx:PlSqlParser.Modify_index_subpartitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_name_old.
    def enterPartition_name_old(self, ctx:PlSqlParser.Partition_name_oldContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_name_old.
    def exitPartition_name_old(self, ctx:PlSqlParser.Partition_name_oldContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_partition_name.
    def enterNew_partition_name(self, ctx:PlSqlParser.New_partition_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_partition_name.
    def exitNew_partition_name(self, ctx:PlSqlParser.New_partition_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_index_name.
    def enterNew_index_name(self, ctx:PlSqlParser.New_index_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_index_name.
    def exitNew_index_name(self, ctx:PlSqlParser.New_index_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_inmemory_join_group.
    def enterAlter_inmemory_join_group(self, ctx:PlSqlParser.Alter_inmemory_join_groupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_inmemory_join_group.
    def exitAlter_inmemory_join_group(self, ctx:PlSqlParser.Alter_inmemory_join_groupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_user.
    def enterCreate_user(self, ctx:PlSqlParser.Create_userContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_user.
    def exitCreate_user(self, ctx:PlSqlParser.Create_userContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_user.
    def enterAlter_user(self, ctx:PlSqlParser.Alter_userContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_user.
    def exitAlter_user(self, ctx:PlSqlParser.Alter_userContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_user.
    def enterDrop_user(self, ctx:PlSqlParser.Drop_userContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_user.
    def exitDrop_user(self, ctx:PlSqlParser.Drop_userContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_identified_by.
    def enterAlter_identified_by(self, ctx:PlSqlParser.Alter_identified_byContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_identified_by.
    def exitAlter_identified_by(self, ctx:PlSqlParser.Alter_identified_byContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identified_by.
    def enterIdentified_by(self, ctx:PlSqlParser.Identified_byContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identified_by.
    def exitIdentified_by(self, ctx:PlSqlParser.Identified_byContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identified_other_clause.
    def enterIdentified_other_clause(self, ctx:PlSqlParser.Identified_other_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identified_other_clause.
    def exitIdentified_other_clause(self, ctx:PlSqlParser.Identified_other_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_tablespace_clause.
    def enterUser_tablespace_clause(self, ctx:PlSqlParser.User_tablespace_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_tablespace_clause.
    def exitUser_tablespace_clause(self, ctx:PlSqlParser.User_tablespace_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quota_clause.
    def enterQuota_clause(self, ctx:PlSqlParser.Quota_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quota_clause.
    def exitQuota_clause(self, ctx:PlSqlParser.Quota_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#profile_clause.
    def enterProfile_clause(self, ctx:PlSqlParser.Profile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#profile_clause.
    def exitProfile_clause(self, ctx:PlSqlParser.Profile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#role_clause.
    def enterRole_clause(self, ctx:PlSqlParser.Role_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#role_clause.
    def exitRole_clause(self, ctx:PlSqlParser.Role_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_default_role_clause.
    def enterUser_default_role_clause(self, ctx:PlSqlParser.User_default_role_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_default_role_clause.
    def exitUser_default_role_clause(self, ctx:PlSqlParser.User_default_role_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#password_expire_clause.
    def enterPassword_expire_clause(self, ctx:PlSqlParser.Password_expire_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#password_expire_clause.
    def exitPassword_expire_clause(self, ctx:PlSqlParser.Password_expire_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_lock_clause.
    def enterUser_lock_clause(self, ctx:PlSqlParser.User_lock_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_lock_clause.
    def exitUser_lock_clause(self, ctx:PlSqlParser.User_lock_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_editions_clause.
    def enterUser_editions_clause(self, ctx:PlSqlParser.User_editions_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_editions_clause.
    def exitUser_editions_clause(self, ctx:PlSqlParser.User_editions_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_user_editions_clause.
    def enterAlter_user_editions_clause(self, ctx:PlSqlParser.Alter_user_editions_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_user_editions_clause.
    def exitAlter_user_editions_clause(self, ctx:PlSqlParser.Alter_user_editions_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#proxy_clause.
    def enterProxy_clause(self, ctx:PlSqlParser.Proxy_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#proxy_clause.
    def exitProxy_clause(self, ctx:PlSqlParser.Proxy_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#container_names.
    def enterContainer_names(self, ctx:PlSqlParser.Container_namesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#container_names.
    def exitContainer_names(self, ctx:PlSqlParser.Container_namesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_container_data.
    def enterSet_container_data(self, ctx:PlSqlParser.Set_container_dataContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_container_data.
    def exitSet_container_data(self, ctx:PlSqlParser.Set_container_dataContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_rem_container_data.
    def enterAdd_rem_container_data(self, ctx:PlSqlParser.Add_rem_container_dataContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_rem_container_data.
    def exitAdd_rem_container_data(self, ctx:PlSqlParser.Add_rem_container_dataContext):
        pass


    # Enter a parse tree produced by PlSqlParser#container_data_clause.
    def enterContainer_data_clause(self, ctx:PlSqlParser.Container_data_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#container_data_clause.
    def exitContainer_data_clause(self, ctx:PlSqlParser.Container_data_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#administer_key_management.
    def enterAdminister_key_management(self, ctx:PlSqlParser.Administer_key_managementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#administer_key_management.
    def exitAdminister_key_management(self, ctx:PlSqlParser.Administer_key_managementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#keystore_management_clauses.
    def enterKeystore_management_clauses(self, ctx:PlSqlParser.Keystore_management_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#keystore_management_clauses.
    def exitKeystore_management_clauses(self, ctx:PlSqlParser.Keystore_management_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_keystore.
    def enterCreate_keystore(self, ctx:PlSqlParser.Create_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_keystore.
    def exitCreate_keystore(self, ctx:PlSqlParser.Create_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#open_keystore.
    def enterOpen_keystore(self, ctx:PlSqlParser.Open_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#open_keystore.
    def exitOpen_keystore(self, ctx:PlSqlParser.Open_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#force_keystore.
    def enterForce_keystore(self, ctx:PlSqlParser.Force_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#force_keystore.
    def exitForce_keystore(self, ctx:PlSqlParser.Force_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#close_keystore.
    def enterClose_keystore(self, ctx:PlSqlParser.Close_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#close_keystore.
    def exitClose_keystore(self, ctx:PlSqlParser.Close_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#backup_keystore.
    def enterBackup_keystore(self, ctx:PlSqlParser.Backup_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#backup_keystore.
    def exitBackup_keystore(self, ctx:PlSqlParser.Backup_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_keystore_password.
    def enterAlter_keystore_password(self, ctx:PlSqlParser.Alter_keystore_passwordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_keystore_password.
    def exitAlter_keystore_password(self, ctx:PlSqlParser.Alter_keystore_passwordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_into_new_keystore.
    def enterMerge_into_new_keystore(self, ctx:PlSqlParser.Merge_into_new_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_into_new_keystore.
    def exitMerge_into_new_keystore(self, ctx:PlSqlParser.Merge_into_new_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_into_existing_keystore.
    def enterMerge_into_existing_keystore(self, ctx:PlSqlParser.Merge_into_existing_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_into_existing_keystore.
    def exitMerge_into_existing_keystore(self, ctx:PlSqlParser.Merge_into_existing_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#isolate_keystore.
    def enterIsolate_keystore(self, ctx:PlSqlParser.Isolate_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#isolate_keystore.
    def exitIsolate_keystore(self, ctx:PlSqlParser.Isolate_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unite_keystore.
    def enterUnite_keystore(self, ctx:PlSqlParser.Unite_keystoreContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unite_keystore.
    def exitUnite_keystore(self, ctx:PlSqlParser.Unite_keystoreContext):
        pass


    # Enter a parse tree produced by PlSqlParser#key_management_clauses.
    def enterKey_management_clauses(self, ctx:PlSqlParser.Key_management_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#key_management_clauses.
    def exitKey_management_clauses(self, ctx:PlSqlParser.Key_management_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_key.
    def enterSet_key(self, ctx:PlSqlParser.Set_keyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_key.
    def exitSet_key(self, ctx:PlSqlParser.Set_keyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_key.
    def enterCreate_key(self, ctx:PlSqlParser.Create_keyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_key.
    def exitCreate_key(self, ctx:PlSqlParser.Create_keyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mkid.
    def enterMkid(self, ctx:PlSqlParser.MkidContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mkid.
    def exitMkid(self, ctx:PlSqlParser.MkidContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mk.
    def enterMk(self, ctx:PlSqlParser.MkContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mk.
    def exitMk(self, ctx:PlSqlParser.MkContext):
        pass


    # Enter a parse tree produced by PlSqlParser#use_key.
    def enterUse_key(self, ctx:PlSqlParser.Use_keyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#use_key.
    def exitUse_key(self, ctx:PlSqlParser.Use_keyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_key_tag.
    def enterSet_key_tag(self, ctx:PlSqlParser.Set_key_tagContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_key_tag.
    def exitSet_key_tag(self, ctx:PlSqlParser.Set_key_tagContext):
        pass


    # Enter a parse tree produced by PlSqlParser#export_keys.
    def enterExport_keys(self, ctx:PlSqlParser.Export_keysContext):
        pass

    # Exit a parse tree produced by PlSqlParser#export_keys.
    def exitExport_keys(self, ctx:PlSqlParser.Export_keysContext):
        pass


    # Enter a parse tree produced by PlSqlParser#import_keys.
    def enterImport_keys(self, ctx:PlSqlParser.Import_keysContext):
        pass

    # Exit a parse tree produced by PlSqlParser#import_keys.
    def exitImport_keys(self, ctx:PlSqlParser.Import_keysContext):
        pass


    # Enter a parse tree produced by PlSqlParser#migrate_keys.
    def enterMigrate_keys(self, ctx:PlSqlParser.Migrate_keysContext):
        pass

    # Exit a parse tree produced by PlSqlParser#migrate_keys.
    def exitMigrate_keys(self, ctx:PlSqlParser.Migrate_keysContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reverse_migrate_keys.
    def enterReverse_migrate_keys(self, ctx:PlSqlParser.Reverse_migrate_keysContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reverse_migrate_keys.
    def exitReverse_migrate_keys(self, ctx:PlSqlParser.Reverse_migrate_keysContext):
        pass


    # Enter a parse tree produced by PlSqlParser#move_keys.
    def enterMove_keys(self, ctx:PlSqlParser.Move_keysContext):
        pass

    # Exit a parse tree produced by PlSqlParser#move_keys.
    def exitMove_keys(self, ctx:PlSqlParser.Move_keysContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identified_by_store.
    def enterIdentified_by_store(self, ctx:PlSqlParser.Identified_by_storeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identified_by_store.
    def exitIdentified_by_store(self, ctx:PlSqlParser.Identified_by_storeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_algorithm_clause.
    def enterUsing_algorithm_clause(self, ctx:PlSqlParser.Using_algorithm_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_algorithm_clause.
    def exitUsing_algorithm_clause(self, ctx:PlSqlParser.Using_algorithm_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_tag_clause.
    def enterUsing_tag_clause(self, ctx:PlSqlParser.Using_tag_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_tag_clause.
    def exitUsing_tag_clause(self, ctx:PlSqlParser.Using_tag_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#secret_management_clauses.
    def enterSecret_management_clauses(self, ctx:PlSqlParser.Secret_management_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#secret_management_clauses.
    def exitSecret_management_clauses(self, ctx:PlSqlParser.Secret_management_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_update_secret.
    def enterAdd_update_secret(self, ctx:PlSqlParser.Add_update_secretContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_update_secret.
    def exitAdd_update_secret(self, ctx:PlSqlParser.Add_update_secretContext):
        pass


    # Enter a parse tree produced by PlSqlParser#delete_secret.
    def enterDelete_secret(self, ctx:PlSqlParser.Delete_secretContext):
        pass

    # Exit a parse tree produced by PlSqlParser#delete_secret.
    def exitDelete_secret(self, ctx:PlSqlParser.Delete_secretContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_update_secret_seps.
    def enterAdd_update_secret_seps(self, ctx:PlSqlParser.Add_update_secret_sepsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_update_secret_seps.
    def exitAdd_update_secret_seps(self, ctx:PlSqlParser.Add_update_secret_sepsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#delete_secret_seps.
    def enterDelete_secret_seps(self, ctx:PlSqlParser.Delete_secret_sepsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#delete_secret_seps.
    def exitDelete_secret_seps(self, ctx:PlSqlParser.Delete_secret_sepsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#zero_downtime_software_patching_clauses.
    def enterZero_downtime_software_patching_clauses(self, ctx:PlSqlParser.Zero_downtime_software_patching_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#zero_downtime_software_patching_clauses.
    def exitZero_downtime_software_patching_clauses(self, ctx:PlSqlParser.Zero_downtime_software_patching_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#with_backup_clause.
    def enterWith_backup_clause(self, ctx:PlSqlParser.With_backup_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#with_backup_clause.
    def exitWith_backup_clause(self, ctx:PlSqlParser.With_backup_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identified_by_password_clause.
    def enterIdentified_by_password_clause(self, ctx:PlSqlParser.Identified_by_password_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identified_by_password_clause.
    def exitIdentified_by_password_clause(self, ctx:PlSqlParser.Identified_by_password_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#keystore_password.
    def enterKeystore_password(self, ctx:PlSqlParser.Keystore_passwordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#keystore_password.
    def exitKeystore_password(self, ctx:PlSqlParser.Keystore_passwordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#path.
    def enterPath(self, ctx:PlSqlParser.PathContext):
        pass

    # Exit a parse tree produced by PlSqlParser#path.
    def exitPath(self, ctx:PlSqlParser.PathContext):
        pass


    # Enter a parse tree produced by PlSqlParser#secret.
    def enterSecret(self, ctx:PlSqlParser.SecretContext):
        pass

    # Exit a parse tree produced by PlSqlParser#secret.
    def exitSecret(self, ctx:PlSqlParser.SecretContext):
        pass


    # Enter a parse tree produced by PlSqlParser#analyze.
    def enterAnalyze(self, ctx:PlSqlParser.AnalyzeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#analyze.
    def exitAnalyze(self, ctx:PlSqlParser.AnalyzeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_extention_clause.
    def enterPartition_extention_clause(self, ctx:PlSqlParser.Partition_extention_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_extention_clause.
    def exitPartition_extention_clause(self, ctx:PlSqlParser.Partition_extention_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#validation_clauses.
    def enterValidation_clauses(self, ctx:PlSqlParser.Validation_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#validation_clauses.
    def exitValidation_clauses(self, ctx:PlSqlParser.Validation_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compute_clauses.
    def enterCompute_clauses(self, ctx:PlSqlParser.Compute_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compute_clauses.
    def exitCompute_clauses(self, ctx:PlSqlParser.Compute_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_clause.
    def enterFor_clause(self, ctx:PlSqlParser.For_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_clause.
    def exitFor_clause(self, ctx:PlSqlParser.For_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#online_or_offline.
    def enterOnline_or_offline(self, ctx:PlSqlParser.Online_or_offlineContext):
        pass

    # Exit a parse tree produced by PlSqlParser#online_or_offline.
    def exitOnline_or_offline(self, ctx:PlSqlParser.Online_or_offlineContext):
        pass


    # Enter a parse tree produced by PlSqlParser#into_clause1.
    def enterInto_clause1(self, ctx:PlSqlParser.Into_clause1Context):
        pass

    # Exit a parse tree produced by PlSqlParser#into_clause1.
    def exitInto_clause1(self, ctx:PlSqlParser.Into_clause1Context):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_key_value.
    def enterPartition_key_value(self, ctx:PlSqlParser.Partition_key_valueContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_key_value.
    def exitPartition_key_value(self, ctx:PlSqlParser.Partition_key_valueContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_key_value.
    def enterSubpartition_key_value(self, ctx:PlSqlParser.Subpartition_key_valueContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_key_value.
    def exitSubpartition_key_value(self, ctx:PlSqlParser.Subpartition_key_valueContext):
        pass


    # Enter a parse tree produced by PlSqlParser#associate_statistics.
    def enterAssociate_statistics(self, ctx:PlSqlParser.Associate_statisticsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#associate_statistics.
    def exitAssociate_statistics(self, ctx:PlSqlParser.Associate_statisticsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_association.
    def enterColumn_association(self, ctx:PlSqlParser.Column_associationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_association.
    def exitColumn_association(self, ctx:PlSqlParser.Column_associationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_association.
    def enterFunction_association(self, ctx:PlSqlParser.Function_associationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_association.
    def exitFunction_association(self, ctx:PlSqlParser.Function_associationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#indextype_name.
    def enterIndextype_name(self, ctx:PlSqlParser.Indextype_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#indextype_name.
    def exitIndextype_name(self, ctx:PlSqlParser.Indextype_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_statistics_type.
    def enterUsing_statistics_type(self, ctx:PlSqlParser.Using_statistics_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_statistics_type.
    def exitUsing_statistics_type(self, ctx:PlSqlParser.Using_statistics_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#statistics_type_name.
    def enterStatistics_type_name(self, ctx:PlSqlParser.Statistics_type_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#statistics_type_name.
    def exitStatistics_type_name(self, ctx:PlSqlParser.Statistics_type_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_cost_clause.
    def enterDefault_cost_clause(self, ctx:PlSqlParser.Default_cost_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_cost_clause.
    def exitDefault_cost_clause(self, ctx:PlSqlParser.Default_cost_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cpu_cost.
    def enterCpu_cost(self, ctx:PlSqlParser.Cpu_costContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cpu_cost.
    def exitCpu_cost(self, ctx:PlSqlParser.Cpu_costContext):
        pass


    # Enter a parse tree produced by PlSqlParser#io_cost.
    def enterIo_cost(self, ctx:PlSqlParser.Io_costContext):
        pass

    # Exit a parse tree produced by PlSqlParser#io_cost.
    def exitIo_cost(self, ctx:PlSqlParser.Io_costContext):
        pass


    # Enter a parse tree produced by PlSqlParser#network_cost.
    def enterNetwork_cost(self, ctx:PlSqlParser.Network_costContext):
        pass

    # Exit a parse tree produced by PlSqlParser#network_cost.
    def exitNetwork_cost(self, ctx:PlSqlParser.Network_costContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_selectivity_clause.
    def enterDefault_selectivity_clause(self, ctx:PlSqlParser.Default_selectivity_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_selectivity_clause.
    def exitDefault_selectivity_clause(self, ctx:PlSqlParser.Default_selectivity_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_selectivity.
    def enterDefault_selectivity(self, ctx:PlSqlParser.Default_selectivityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_selectivity.
    def exitDefault_selectivity(self, ctx:PlSqlParser.Default_selectivityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#storage_table_clause.
    def enterStorage_table_clause(self, ctx:PlSqlParser.Storage_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#storage_table_clause.
    def exitStorage_table_clause(self, ctx:PlSqlParser.Storage_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unified_auditing.
    def enterUnified_auditing(self, ctx:PlSqlParser.Unified_auditingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unified_auditing.
    def exitUnified_auditing(self, ctx:PlSqlParser.Unified_auditingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#policy_name.
    def enterPolicy_name(self, ctx:PlSqlParser.Policy_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#policy_name.
    def exitPolicy_name(self, ctx:PlSqlParser.Policy_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_traditional.
    def enterAudit_traditional(self, ctx:PlSqlParser.Audit_traditionalContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_traditional.
    def exitAudit_traditional(self, ctx:PlSqlParser.Audit_traditionalContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_direct_path.
    def enterAudit_direct_path(self, ctx:PlSqlParser.Audit_direct_pathContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_direct_path.
    def exitAudit_direct_path(self, ctx:PlSqlParser.Audit_direct_pathContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_container_clause.
    def enterAudit_container_clause(self, ctx:PlSqlParser.Audit_container_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_container_clause.
    def exitAudit_container_clause(self, ctx:PlSqlParser.Audit_container_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_operation_clause.
    def enterAudit_operation_clause(self, ctx:PlSqlParser.Audit_operation_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_operation_clause.
    def exitAudit_operation_clause(self, ctx:PlSqlParser.Audit_operation_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#auditing_by_clause.
    def enterAuditing_by_clause(self, ctx:PlSqlParser.Auditing_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#auditing_by_clause.
    def exitAuditing_by_clause(self, ctx:PlSqlParser.Auditing_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_user.
    def enterAudit_user(self, ctx:PlSqlParser.Audit_userContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_user.
    def exitAudit_user(self, ctx:PlSqlParser.Audit_userContext):
        pass


    # Enter a parse tree produced by PlSqlParser#audit_schema_object_clause.
    def enterAudit_schema_object_clause(self, ctx:PlSqlParser.Audit_schema_object_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#audit_schema_object_clause.
    def exitAudit_schema_object_clause(self, ctx:PlSqlParser.Audit_schema_object_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_operation.
    def enterSql_operation(self, ctx:PlSqlParser.Sql_operationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_operation.
    def exitSql_operation(self, ctx:PlSqlParser.Sql_operationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#auditing_on_clause.
    def enterAuditing_on_clause(self, ctx:PlSqlParser.Auditing_on_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#auditing_on_clause.
    def exitAuditing_on_clause(self, ctx:PlSqlParser.Auditing_on_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_name.
    def enterModel_name(self, ctx:PlSqlParser.Model_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_name.
    def exitModel_name(self, ctx:PlSqlParser.Model_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_name.
    def enterObject_name(self, ctx:PlSqlParser.Object_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_name.
    def exitObject_name(self, ctx:PlSqlParser.Object_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#profile_name.
    def enterProfile_name(self, ctx:PlSqlParser.Profile_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#profile_name.
    def exitProfile_name(self, ctx:PlSqlParser.Profile_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_statement_shortcut.
    def enterSql_statement_shortcut(self, ctx:PlSqlParser.Sql_statement_shortcutContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_statement_shortcut.
    def exitSql_statement_shortcut(self, ctx:PlSqlParser.Sql_statement_shortcutContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_index.
    def enterDrop_index(self, ctx:PlSqlParser.Drop_indexContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_index.
    def exitDrop_index(self, ctx:PlSqlParser.Drop_indexContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disassociate_statistics.
    def enterDisassociate_statistics(self, ctx:PlSqlParser.Disassociate_statisticsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disassociate_statistics.
    def exitDisassociate_statistics(self, ctx:PlSqlParser.Disassociate_statisticsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_indextype.
    def enterDrop_indextype(self, ctx:PlSqlParser.Drop_indextypeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_indextype.
    def exitDrop_indextype(self, ctx:PlSqlParser.Drop_indextypeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_inmemory_join_group.
    def enterDrop_inmemory_join_group(self, ctx:PlSqlParser.Drop_inmemory_join_groupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_inmemory_join_group.
    def exitDrop_inmemory_join_group(self, ctx:PlSqlParser.Drop_inmemory_join_groupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_table.
    def enterFlashback_table(self, ctx:PlSqlParser.Flashback_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_table.
    def exitFlashback_table(self, ctx:PlSqlParser.Flashback_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#restore_point.
    def enterRestore_point(self, ctx:PlSqlParser.Restore_pointContext):
        pass

    # Exit a parse tree produced by PlSqlParser#restore_point.
    def exitRestore_point(self, ctx:PlSqlParser.Restore_pointContext):
        pass


    # Enter a parse tree produced by PlSqlParser#purge_statement.
    def enterPurge_statement(self, ctx:PlSqlParser.Purge_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#purge_statement.
    def exitPurge_statement(self, ctx:PlSqlParser.Purge_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#noaudit_statement.
    def enterNoaudit_statement(self, ctx:PlSqlParser.Noaudit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#noaudit_statement.
    def exitNoaudit_statement(self, ctx:PlSqlParser.Noaudit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rename_object.
    def enterRename_object(self, ctx:PlSqlParser.Rename_objectContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rename_object.
    def exitRename_object(self, ctx:PlSqlParser.Rename_objectContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grant_statement.
    def enterGrant_statement(self, ctx:PlSqlParser.Grant_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grant_statement.
    def exitGrant_statement(self, ctx:PlSqlParser.Grant_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#container_clause.
    def enterContainer_clause(self, ctx:PlSqlParser.Container_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#container_clause.
    def exitContainer_clause(self, ctx:PlSqlParser.Container_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#revoke_statement.
    def enterRevoke_statement(self, ctx:PlSqlParser.Revoke_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#revoke_statement.
    def exitRevoke_statement(self, ctx:PlSqlParser.Revoke_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#revoke_system_privilege.
    def enterRevoke_system_privilege(self, ctx:PlSqlParser.Revoke_system_privilegeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#revoke_system_privilege.
    def exitRevoke_system_privilege(self, ctx:PlSqlParser.Revoke_system_privilegeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#revokee_clause.
    def enterRevokee_clause(self, ctx:PlSqlParser.Revokee_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#revokee_clause.
    def exitRevokee_clause(self, ctx:PlSqlParser.Revokee_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#revoke_object_privileges.
    def enterRevoke_object_privileges(self, ctx:PlSqlParser.Revoke_object_privilegesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#revoke_object_privileges.
    def exitRevoke_object_privileges(self, ctx:PlSqlParser.Revoke_object_privilegesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_object_clause.
    def enterOn_object_clause(self, ctx:PlSqlParser.On_object_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_object_clause.
    def exitOn_object_clause(self, ctx:PlSqlParser.On_object_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#revoke_roles_from_programs.
    def enterRevoke_roles_from_programs(self, ctx:PlSqlParser.Revoke_roles_from_programsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#revoke_roles_from_programs.
    def exitRevoke_roles_from_programs(self, ctx:PlSqlParser.Revoke_roles_from_programsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#program_unit.
    def enterProgram_unit(self, ctx:PlSqlParser.Program_unitContext):
        pass

    # Exit a parse tree produced by PlSqlParser#program_unit.
    def exitProgram_unit(self, ctx:PlSqlParser.Program_unitContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_dimension.
    def enterCreate_dimension(self, ctx:PlSqlParser.Create_dimensionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_dimension.
    def exitCreate_dimension(self, ctx:PlSqlParser.Create_dimensionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_directory.
    def enterCreate_directory(self, ctx:PlSqlParser.Create_directoryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_directory.
    def exitCreate_directory(self, ctx:PlSqlParser.Create_directoryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#directory_name.
    def enterDirectory_name(self, ctx:PlSqlParser.Directory_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#directory_name.
    def exitDirectory_name(self, ctx:PlSqlParser.Directory_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#directory_path.
    def enterDirectory_path(self, ctx:PlSqlParser.Directory_pathContext):
        pass

    # Exit a parse tree produced by PlSqlParser#directory_path.
    def exitDirectory_path(self, ctx:PlSqlParser.Directory_pathContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_inmemory_join_group.
    def enterCreate_inmemory_join_group(self, ctx:PlSqlParser.Create_inmemory_join_groupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_inmemory_join_group.
    def exitCreate_inmemory_join_group(self, ctx:PlSqlParser.Create_inmemory_join_groupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_hierarchy.
    def enterDrop_hierarchy(self, ctx:PlSqlParser.Drop_hierarchyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_hierarchy.
    def exitDrop_hierarchy(self, ctx:PlSqlParser.Drop_hierarchyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_library.
    def enterAlter_library(self, ctx:PlSqlParser.Alter_libraryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_library.
    def exitAlter_library(self, ctx:PlSqlParser.Alter_libraryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_java.
    def enterDrop_java(self, ctx:PlSqlParser.Drop_javaContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_java.
    def exitDrop_java(self, ctx:PlSqlParser.Drop_javaContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_library.
    def enterDrop_library(self, ctx:PlSqlParser.Drop_libraryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_library.
    def exitDrop_library(self, ctx:PlSqlParser.Drop_libraryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_java.
    def enterCreate_java(self, ctx:PlSqlParser.Create_javaContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_java.
    def exitCreate_java(self, ctx:PlSqlParser.Create_javaContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_library.
    def enterCreate_library(self, ctx:PlSqlParser.Create_libraryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_library.
    def exitCreate_library(self, ctx:PlSqlParser.Create_libraryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#plsql_library_source.
    def enterPlsql_library_source(self, ctx:PlSqlParser.Plsql_library_sourceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#plsql_library_source.
    def exitPlsql_library_source(self, ctx:PlSqlParser.Plsql_library_sourceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#credential_name.
    def enterCredential_name(self, ctx:PlSqlParser.Credential_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#credential_name.
    def exitCredential_name(self, ctx:PlSqlParser.Credential_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#library_editionable.
    def enterLibrary_editionable(self, ctx:PlSqlParser.Library_editionableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#library_editionable.
    def exitLibrary_editionable(self, ctx:PlSqlParser.Library_editionableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#library_debug.
    def enterLibrary_debug(self, ctx:PlSqlParser.Library_debugContext):
        pass

    # Exit a parse tree produced by PlSqlParser#library_debug.
    def exitLibrary_debug(self, ctx:PlSqlParser.Library_debugContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compiler_parameters_clause.
    def enterCompiler_parameters_clause(self, ctx:PlSqlParser.Compiler_parameters_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compiler_parameters_clause.
    def exitCompiler_parameters_clause(self, ctx:PlSqlParser.Compiler_parameters_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter_value.
    def enterParameter_value(self, ctx:PlSqlParser.Parameter_valueContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter_value.
    def exitParameter_value(self, ctx:PlSqlParser.Parameter_valueContext):
        pass


    # Enter a parse tree produced by PlSqlParser#library_name.
    def enterLibrary_name(self, ctx:PlSqlParser.Library_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#library_name.
    def exitLibrary_name(self, ctx:PlSqlParser.Library_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_dimension.
    def enterAlter_dimension(self, ctx:PlSqlParser.Alter_dimensionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_dimension.
    def exitAlter_dimension(self, ctx:PlSqlParser.Alter_dimensionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#level_clause.
    def enterLevel_clause(self, ctx:PlSqlParser.Level_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#level_clause.
    def exitLevel_clause(self, ctx:PlSqlParser.Level_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hierarchy_clause.
    def enterHierarchy_clause(self, ctx:PlSqlParser.Hierarchy_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hierarchy_clause.
    def exitHierarchy_clause(self, ctx:PlSqlParser.Hierarchy_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dimension_join_clause.
    def enterDimension_join_clause(self, ctx:PlSqlParser.Dimension_join_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dimension_join_clause.
    def exitDimension_join_clause(self, ctx:PlSqlParser.Dimension_join_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_clause.
    def enterAttribute_clause(self, ctx:PlSqlParser.Attribute_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_clause.
    def exitAttribute_clause(self, ctx:PlSqlParser.Attribute_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#extended_attribute_clause.
    def enterExtended_attribute_clause(self, ctx:PlSqlParser.Extended_attribute_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#extended_attribute_clause.
    def exitExtended_attribute_clause(self, ctx:PlSqlParser.Extended_attribute_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_one_or_more_sub_clause.
    def enterColumn_one_or_more_sub_clause(self, ctx:PlSqlParser.Column_one_or_more_sub_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_one_or_more_sub_clause.
    def exitColumn_one_or_more_sub_clause(self, ctx:PlSqlParser.Column_one_or_more_sub_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_view.
    def enterAlter_view(self, ctx:PlSqlParser.Alter_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_view.
    def exitAlter_view(self, ctx:PlSqlParser.Alter_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_view_editionable.
    def enterAlter_view_editionable(self, ctx:PlSqlParser.Alter_view_editionableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_view_editionable.
    def exitAlter_view_editionable(self, ctx:PlSqlParser.Alter_view_editionableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_view.
    def enterCreate_view(self, ctx:PlSqlParser.Create_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_view.
    def exitCreate_view(self, ctx:PlSqlParser.Create_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#editioning_clause.
    def enterEditioning_clause(self, ctx:PlSqlParser.Editioning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#editioning_clause.
    def exitEditioning_clause(self, ctx:PlSqlParser.Editioning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#view_options.
    def enterView_options(self, ctx:PlSqlParser.View_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#view_options.
    def exitView_options(self, ctx:PlSqlParser.View_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#view_alias_constraint.
    def enterView_alias_constraint(self, ctx:PlSqlParser.View_alias_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#view_alias_constraint.
    def exitView_alias_constraint(self, ctx:PlSqlParser.View_alias_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_view_clause.
    def enterObject_view_clause(self, ctx:PlSqlParser.Object_view_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_view_clause.
    def exitObject_view_clause(self, ctx:PlSqlParser.Object_view_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inline_constraint.
    def enterInline_constraint(self, ctx:PlSqlParser.Inline_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inline_constraint.
    def exitInline_constraint(self, ctx:PlSqlParser.Inline_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inline_ref_constraint.
    def enterInline_ref_constraint(self, ctx:PlSqlParser.Inline_ref_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inline_ref_constraint.
    def exitInline_ref_constraint(self, ctx:PlSqlParser.Inline_ref_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#out_of_line_ref_constraint.
    def enterOut_of_line_ref_constraint(self, ctx:PlSqlParser.Out_of_line_ref_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#out_of_line_ref_constraint.
    def exitOut_of_line_ref_constraint(self, ctx:PlSqlParser.Out_of_line_ref_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#out_of_line_constraint.
    def enterOut_of_line_constraint(self, ctx:PlSqlParser.Out_of_line_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#out_of_line_constraint.
    def exitOut_of_line_constraint(self, ctx:PlSqlParser.Out_of_line_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constraint_state.
    def enterConstraint_state(self, ctx:PlSqlParser.Constraint_stateContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constraint_state.
    def exitConstraint_state(self, ctx:PlSqlParser.Constraint_stateContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltype_view_clause.
    def enterXmltype_view_clause(self, ctx:PlSqlParser.Xmltype_view_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltype_view_clause.
    def exitXmltype_view_clause(self, ctx:PlSqlParser.Xmltype_view_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_schema_spec.
    def enterXml_schema_spec(self, ctx:PlSqlParser.Xml_schema_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_schema_spec.
    def exitXml_schema_spec(self, ctx:PlSqlParser.Xml_schema_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_schema_url.
    def enterXml_schema_url(self, ctx:PlSqlParser.Xml_schema_urlContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_schema_url.
    def exitXml_schema_url(self, ctx:PlSqlParser.Xml_schema_urlContext):
        pass


    # Enter a parse tree produced by PlSqlParser#element.
    def enterElement(self, ctx:PlSqlParser.ElementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#element.
    def exitElement(self, ctx:PlSqlParser.ElementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_tablespace.
    def enterAlter_tablespace(self, ctx:PlSqlParser.Alter_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_tablespace.
    def exitAlter_tablespace(self, ctx:PlSqlParser.Alter_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datafile_tempfile_clauses.
    def enterDatafile_tempfile_clauses(self, ctx:PlSqlParser.Datafile_tempfile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datafile_tempfile_clauses.
    def exitDatafile_tempfile_clauses(self, ctx:PlSqlParser.Datafile_tempfile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_logging_clauses.
    def enterTablespace_logging_clauses(self, ctx:PlSqlParser.Tablespace_logging_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_logging_clauses.
    def exitTablespace_logging_clauses(self, ctx:PlSqlParser.Tablespace_logging_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_group_clause.
    def enterTablespace_group_clause(self, ctx:PlSqlParser.Tablespace_group_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_group_clause.
    def exitTablespace_group_clause(self, ctx:PlSqlParser.Tablespace_group_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_group_name.
    def enterTablespace_group_name(self, ctx:PlSqlParser.Tablespace_group_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_group_name.
    def exitTablespace_group_name(self, ctx:PlSqlParser.Tablespace_group_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_state_clauses.
    def enterTablespace_state_clauses(self, ctx:PlSqlParser.Tablespace_state_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_state_clauses.
    def exitTablespace_state_clauses(self, ctx:PlSqlParser.Tablespace_state_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_mode_clause.
    def enterFlashback_mode_clause(self, ctx:PlSqlParser.Flashback_mode_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_mode_clause.
    def exitFlashback_mode_clause(self, ctx:PlSqlParser.Flashback_mode_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_tablespace_name.
    def enterNew_tablespace_name(self, ctx:PlSqlParser.New_tablespace_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_tablespace_name.
    def exitNew_tablespace_name(self, ctx:PlSqlParser.New_tablespace_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_tablespace.
    def enterCreate_tablespace(self, ctx:PlSqlParser.Create_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_tablespace.
    def exitCreate_tablespace(self, ctx:PlSqlParser.Create_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#permanent_tablespace_clause.
    def enterPermanent_tablespace_clause(self, ctx:PlSqlParser.Permanent_tablespace_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#permanent_tablespace_clause.
    def exitPermanent_tablespace_clause(self, ctx:PlSqlParser.Permanent_tablespace_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_encryption_spec.
    def enterTablespace_encryption_spec(self, ctx:PlSqlParser.Tablespace_encryption_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_encryption_spec.
    def exitTablespace_encryption_spec(self, ctx:PlSqlParser.Tablespace_encryption_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logging_clause.
    def enterLogging_clause(self, ctx:PlSqlParser.Logging_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logging_clause.
    def exitLogging_clause(self, ctx:PlSqlParser.Logging_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#extent_management_clause.
    def enterExtent_management_clause(self, ctx:PlSqlParser.Extent_management_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#extent_management_clause.
    def exitExtent_management_clause(self, ctx:PlSqlParser.Extent_management_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#segment_management_clause.
    def enterSegment_management_clause(self, ctx:PlSqlParser.Segment_management_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#segment_management_clause.
    def exitSegment_management_clause(self, ctx:PlSqlParser.Segment_management_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#temporary_tablespace_clause.
    def enterTemporary_tablespace_clause(self, ctx:PlSqlParser.Temporary_tablespace_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#temporary_tablespace_clause.
    def exitTemporary_tablespace_clause(self, ctx:PlSqlParser.Temporary_tablespace_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#undo_tablespace_clause.
    def enterUndo_tablespace_clause(self, ctx:PlSqlParser.Undo_tablespace_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#undo_tablespace_clause.
    def exitUndo_tablespace_clause(self, ctx:PlSqlParser.Undo_tablespace_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_retention_clause.
    def enterTablespace_retention_clause(self, ctx:PlSqlParser.Tablespace_retention_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_retention_clause.
    def exitTablespace_retention_clause(self, ctx:PlSqlParser.Tablespace_retention_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_tablespace_set.
    def enterCreate_tablespace_set(self, ctx:PlSqlParser.Create_tablespace_setContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_tablespace_set.
    def exitCreate_tablespace_set(self, ctx:PlSqlParser.Create_tablespace_setContext):
        pass


    # Enter a parse tree produced by PlSqlParser#permanent_tablespace_attrs.
    def enterPermanent_tablespace_attrs(self, ctx:PlSqlParser.Permanent_tablespace_attrsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#permanent_tablespace_attrs.
    def exitPermanent_tablespace_attrs(self, ctx:PlSqlParser.Permanent_tablespace_attrsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_encryption_clause.
    def enterTablespace_encryption_clause(self, ctx:PlSqlParser.Tablespace_encryption_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_encryption_clause.
    def exitTablespace_encryption_clause(self, ctx:PlSqlParser.Tablespace_encryption_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_tablespace_params.
    def enterDefault_tablespace_params(self, ctx:PlSqlParser.Default_tablespace_paramsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_tablespace_params.
    def exitDefault_tablespace_params(self, ctx:PlSqlParser.Default_tablespace_paramsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_table_compression.
    def enterDefault_table_compression(self, ctx:PlSqlParser.Default_table_compressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_table_compression.
    def exitDefault_table_compression(self, ctx:PlSqlParser.Default_table_compressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#low_high.
    def enterLow_high(self, ctx:PlSqlParser.Low_highContext):
        pass

    # Exit a parse tree produced by PlSqlParser#low_high.
    def exitLow_high(self, ctx:PlSqlParser.Low_highContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_index_compression.
    def enterDefault_index_compression(self, ctx:PlSqlParser.Default_index_compressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_index_compression.
    def exitDefault_index_compression(self, ctx:PlSqlParser.Default_index_compressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmmemory_clause.
    def enterInmmemory_clause(self, ctx:PlSqlParser.Inmmemory_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmmemory_clause.
    def exitInmmemory_clause(self, ctx:PlSqlParser.Inmmemory_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datafile_specification.
    def enterDatafile_specification(self, ctx:PlSqlParser.Datafile_specificationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datafile_specification.
    def exitDatafile_specification(self, ctx:PlSqlParser.Datafile_specificationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tempfile_specification.
    def enterTempfile_specification(self, ctx:PlSqlParser.Tempfile_specificationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tempfile_specification.
    def exitTempfile_specification(self, ctx:PlSqlParser.Tempfile_specificationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datafile_tempfile_spec.
    def enterDatafile_tempfile_spec(self, ctx:PlSqlParser.Datafile_tempfile_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datafile_tempfile_spec.
    def exitDatafile_tempfile_spec(self, ctx:PlSqlParser.Datafile_tempfile_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#redo_log_file_spec.
    def enterRedo_log_file_spec(self, ctx:PlSqlParser.Redo_log_file_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#redo_log_file_spec.
    def exitRedo_log_file_spec(self, ctx:PlSqlParser.Redo_log_file_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#autoextend_clause.
    def enterAutoextend_clause(self, ctx:PlSqlParser.Autoextend_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#autoextend_clause.
    def exitAutoextend_clause(self, ctx:PlSqlParser.Autoextend_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#maxsize_clause.
    def enterMaxsize_clause(self, ctx:PlSqlParser.Maxsize_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#maxsize_clause.
    def exitMaxsize_clause(self, ctx:PlSqlParser.Maxsize_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#build_clause.
    def enterBuild_clause(self, ctx:PlSqlParser.Build_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#build_clause.
    def exitBuild_clause(self, ctx:PlSqlParser.Build_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parallel_clause.
    def enterParallel_clause(self, ctx:PlSqlParser.Parallel_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parallel_clause.
    def exitParallel_clause(self, ctx:PlSqlParser.Parallel_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_materialized_view.
    def enterAlter_materialized_view(self, ctx:PlSqlParser.Alter_materialized_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_materialized_view.
    def exitAlter_materialized_view(self, ctx:PlSqlParser.Alter_materialized_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_mv_option1.
    def enterAlter_mv_option1(self, ctx:PlSqlParser.Alter_mv_option1Context):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_mv_option1.
    def exitAlter_mv_option1(self, ctx:PlSqlParser.Alter_mv_option1Context):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_mv_refresh.
    def enterAlter_mv_refresh(self, ctx:PlSqlParser.Alter_mv_refreshContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_mv_refresh.
    def exitAlter_mv_refresh(self, ctx:PlSqlParser.Alter_mv_refreshContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollback_segment.
    def enterRollback_segment(self, ctx:PlSqlParser.Rollback_segmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollback_segment.
    def exitRollback_segment(self, ctx:PlSqlParser.Rollback_segmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_mv_column_clause.
    def enterModify_mv_column_clause(self, ctx:PlSqlParser.Modify_mv_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_mv_column_clause.
    def exitModify_mv_column_clause(self, ctx:PlSqlParser.Modify_mv_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_materialized_view_log.
    def enterAlter_materialized_view_log(self, ctx:PlSqlParser.Alter_materialized_view_logContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_materialized_view_log.
    def exitAlter_materialized_view_log(self, ctx:PlSqlParser.Alter_materialized_view_logContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_mv_log_column_clause.
    def enterAdd_mv_log_column_clause(self, ctx:PlSqlParser.Add_mv_log_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_mv_log_column_clause.
    def exitAdd_mv_log_column_clause(self, ctx:PlSqlParser.Add_mv_log_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#move_mv_log_clause.
    def enterMove_mv_log_clause(self, ctx:PlSqlParser.Move_mv_log_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#move_mv_log_clause.
    def exitMove_mv_log_clause(self, ctx:PlSqlParser.Move_mv_log_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mv_log_augmentation.
    def enterMv_log_augmentation(self, ctx:PlSqlParser.Mv_log_augmentationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mv_log_augmentation.
    def exitMv_log_augmentation(self, ctx:PlSqlParser.Mv_log_augmentationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datetime_expr.
    def enterDatetime_expr(self, ctx:PlSqlParser.Datetime_exprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datetime_expr.
    def exitDatetime_expr(self, ctx:PlSqlParser.Datetime_exprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#interval_expr.
    def enterInterval_expr(self, ctx:PlSqlParser.Interval_exprContext):
        pass

    # Exit a parse tree produced by PlSqlParser#interval_expr.
    def exitInterval_expr(self, ctx:PlSqlParser.Interval_exprContext):
        pass


    # Enter a parse tree produced by PlSqlParser#synchronous_or_asynchronous.
    def enterSynchronous_or_asynchronous(self, ctx:PlSqlParser.Synchronous_or_asynchronousContext):
        pass

    # Exit a parse tree produced by PlSqlParser#synchronous_or_asynchronous.
    def exitSynchronous_or_asynchronous(self, ctx:PlSqlParser.Synchronous_or_asynchronousContext):
        pass


    # Enter a parse tree produced by PlSqlParser#including_or_excluding.
    def enterIncluding_or_excluding(self, ctx:PlSqlParser.Including_or_excludingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#including_or_excluding.
    def exitIncluding_or_excluding(self, ctx:PlSqlParser.Including_or_excludingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_materialized_view_log.
    def enterCreate_materialized_view_log(self, ctx:PlSqlParser.Create_materialized_view_logContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_materialized_view_log.
    def exitCreate_materialized_view_log(self, ctx:PlSqlParser.Create_materialized_view_logContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_values_clause.
    def enterNew_values_clause(self, ctx:PlSqlParser.New_values_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_values_clause.
    def exitNew_values_clause(self, ctx:PlSqlParser.New_values_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mv_log_purge_clause.
    def enterMv_log_purge_clause(self, ctx:PlSqlParser.Mv_log_purge_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mv_log_purge_clause.
    def exitMv_log_purge_clause(self, ctx:PlSqlParser.Mv_log_purge_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_materialized_zonemap.
    def enterCreate_materialized_zonemap(self, ctx:PlSqlParser.Create_materialized_zonemapContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_materialized_zonemap.
    def exitCreate_materialized_zonemap(self, ctx:PlSqlParser.Create_materialized_zonemapContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_materialized_zonemap.
    def enterAlter_materialized_zonemap(self, ctx:PlSqlParser.Alter_materialized_zonemapContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_materialized_zonemap.
    def exitAlter_materialized_zonemap(self, ctx:PlSqlParser.Alter_materialized_zonemapContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_materialized_zonemap.
    def enterDrop_materialized_zonemap(self, ctx:PlSqlParser.Drop_materialized_zonemapContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_materialized_zonemap.
    def exitDrop_materialized_zonemap(self, ctx:PlSqlParser.Drop_materialized_zonemapContext):
        pass


    # Enter a parse tree produced by PlSqlParser#zonemap_refresh_clause.
    def enterZonemap_refresh_clause(self, ctx:PlSqlParser.Zonemap_refresh_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#zonemap_refresh_clause.
    def exitZonemap_refresh_clause(self, ctx:PlSqlParser.Zonemap_refresh_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#zonemap_attributes.
    def enterZonemap_attributes(self, ctx:PlSqlParser.Zonemap_attributesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#zonemap_attributes.
    def exitZonemap_attributes(self, ctx:PlSqlParser.Zonemap_attributesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#zonemap_name.
    def enterZonemap_name(self, ctx:PlSqlParser.Zonemap_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#zonemap_name.
    def exitZonemap_name(self, ctx:PlSqlParser.Zonemap_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#operator_name.
    def enterOperator_name(self, ctx:PlSqlParser.Operator_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#operator_name.
    def exitOperator_name(self, ctx:PlSqlParser.Operator_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#operator_function_name.
    def enterOperator_function_name(self, ctx:PlSqlParser.Operator_function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#operator_function_name.
    def exitOperator_function_name(self, ctx:PlSqlParser.Operator_function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_zonemap_on_table.
    def enterCreate_zonemap_on_table(self, ctx:PlSqlParser.Create_zonemap_on_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_zonemap_on_table.
    def exitCreate_zonemap_on_table(self, ctx:PlSqlParser.Create_zonemap_on_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_zonemap_as_subquery.
    def enterCreate_zonemap_as_subquery(self, ctx:PlSqlParser.Create_zonemap_as_subqueryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_zonemap_as_subquery.
    def exitCreate_zonemap_as_subquery(self, ctx:PlSqlParser.Create_zonemap_as_subqueryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_operator.
    def enterAlter_operator(self, ctx:PlSqlParser.Alter_operatorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_operator.
    def exitAlter_operator(self, ctx:PlSqlParser.Alter_operatorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_operator.
    def enterDrop_operator(self, ctx:PlSqlParser.Drop_operatorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_operator.
    def exitDrop_operator(self, ctx:PlSqlParser.Drop_operatorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_operator.
    def enterCreate_operator(self, ctx:PlSqlParser.Create_operatorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_operator.
    def exitCreate_operator(self, ctx:PlSqlParser.Create_operatorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#binding_clause.
    def enterBinding_clause(self, ctx:PlSqlParser.Binding_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#binding_clause.
    def exitBinding_clause(self, ctx:PlSqlParser.Binding_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_binding_clause.
    def enterAdd_binding_clause(self, ctx:PlSqlParser.Add_binding_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_binding_clause.
    def exitAdd_binding_clause(self, ctx:PlSqlParser.Add_binding_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#implementation_clause.
    def enterImplementation_clause(self, ctx:PlSqlParser.Implementation_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#implementation_clause.
    def exitImplementation_clause(self, ctx:PlSqlParser.Implementation_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#primary_operator_list.
    def enterPrimary_operator_list(self, ctx:PlSqlParser.Primary_operator_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#primary_operator_list.
    def exitPrimary_operator_list(self, ctx:PlSqlParser.Primary_operator_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#primary_operator_item.
    def enterPrimary_operator_item(self, ctx:PlSqlParser.Primary_operator_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#primary_operator_item.
    def exitPrimary_operator_item(self, ctx:PlSqlParser.Primary_operator_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#operator_context_clause.
    def enterOperator_context_clause(self, ctx:PlSqlParser.Operator_context_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#operator_context_clause.
    def exitOperator_context_clause(self, ctx:PlSqlParser.Operator_context_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_function_clause.
    def enterUsing_function_clause(self, ctx:PlSqlParser.Using_function_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_function_clause.
    def exitUsing_function_clause(self, ctx:PlSqlParser.Using_function_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_binding_clause.
    def enterDrop_binding_clause(self, ctx:PlSqlParser.Drop_binding_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_binding_clause.
    def exitDrop_binding_clause(self, ctx:PlSqlParser.Drop_binding_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_materialized_view.
    def enterCreate_materialized_view(self, ctx:PlSqlParser.Create_materialized_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_materialized_view.
    def exitCreate_materialized_view(self, ctx:PlSqlParser.Create_materialized_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#scoped_table_ref_constraint.
    def enterScoped_table_ref_constraint(self, ctx:PlSqlParser.Scoped_table_ref_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#scoped_table_ref_constraint.
    def exitScoped_table_ref_constraint(self, ctx:PlSqlParser.Scoped_table_ref_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mv_column_alias.
    def enterMv_column_alias(self, ctx:PlSqlParser.Mv_column_aliasContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mv_column_alias.
    def exitMv_column_alias(self, ctx:PlSqlParser.Mv_column_aliasContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_mv_refresh.
    def enterCreate_mv_refresh(self, ctx:PlSqlParser.Create_mv_refreshContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_mv_refresh.
    def exitCreate_mv_refresh(self, ctx:PlSqlParser.Create_mv_refreshContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_materialized_view.
    def enterDrop_materialized_view(self, ctx:PlSqlParser.Drop_materialized_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_materialized_view.
    def exitDrop_materialized_view(self, ctx:PlSqlParser.Drop_materialized_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_context.
    def enterCreate_context(self, ctx:PlSqlParser.Create_contextContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_context.
    def exitCreate_context(self, ctx:PlSqlParser.Create_contextContext):
        pass


    # Enter a parse tree produced by PlSqlParser#oracle_namespace.
    def enterOracle_namespace(self, ctx:PlSqlParser.Oracle_namespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#oracle_namespace.
    def exitOracle_namespace(self, ctx:PlSqlParser.Oracle_namespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_cluster.
    def enterCreate_cluster(self, ctx:PlSqlParser.Create_clusterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_cluster.
    def exitCreate_cluster(self, ctx:PlSqlParser.Create_clusterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_profile.
    def enterCreate_profile(self, ctx:PlSqlParser.Create_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_profile.
    def exitCreate_profile(self, ctx:PlSqlParser.Create_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#resource_parameters.
    def enterResource_parameters(self, ctx:PlSqlParser.Resource_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#resource_parameters.
    def exitResource_parameters(self, ctx:PlSqlParser.Resource_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#password_parameters.
    def enterPassword_parameters(self, ctx:PlSqlParser.Password_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#password_parameters.
    def exitPassword_parameters(self, ctx:PlSqlParser.Password_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_lockdown_profile.
    def enterCreate_lockdown_profile(self, ctx:PlSqlParser.Create_lockdown_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_lockdown_profile.
    def exitCreate_lockdown_profile(self, ctx:PlSqlParser.Create_lockdown_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#static_base_profile.
    def enterStatic_base_profile(self, ctx:PlSqlParser.Static_base_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#static_base_profile.
    def exitStatic_base_profile(self, ctx:PlSqlParser.Static_base_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dynamic_base_profile.
    def enterDynamic_base_profile(self, ctx:PlSqlParser.Dynamic_base_profileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dynamic_base_profile.
    def exitDynamic_base_profile(self, ctx:PlSqlParser.Dynamic_base_profileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_outline.
    def enterCreate_outline(self, ctx:PlSqlParser.Create_outlineContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_outline.
    def exitCreate_outline(self, ctx:PlSqlParser.Create_outlineContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_restore_point.
    def enterCreate_restore_point(self, ctx:PlSqlParser.Create_restore_pointContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_restore_point.
    def exitCreate_restore_point(self, ctx:PlSqlParser.Create_restore_pointContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_role.
    def enterCreate_role(self, ctx:PlSqlParser.Create_roleContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_role.
    def exitCreate_role(self, ctx:PlSqlParser.Create_roleContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_table.
    def enterCreate_table(self, ctx:PlSqlParser.Create_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_table.
    def exitCreate_table(self, ctx:PlSqlParser.Create_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltype_table.
    def enterXmltype_table(self, ctx:PlSqlParser.Xmltype_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltype_table.
    def exitXmltype_table(self, ctx:PlSqlParser.Xmltype_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltype_virtual_columns.
    def enterXmltype_virtual_columns(self, ctx:PlSqlParser.Xmltype_virtual_columnsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltype_virtual_columns.
    def exitXmltype_virtual_columns(self, ctx:PlSqlParser.Xmltype_virtual_columnsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltype_column_properties.
    def enterXmltype_column_properties(self, ctx:PlSqlParser.Xmltype_column_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltype_column_properties.
    def exitXmltype_column_properties(self, ctx:PlSqlParser.Xmltype_column_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltype_storage.
    def enterXmltype_storage(self, ctx:PlSqlParser.Xmltype_storageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltype_storage.
    def exitXmltype_storage(self, ctx:PlSqlParser.Xmltype_storageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlschema_spec.
    def enterXmlschema_spec(self, ctx:PlSqlParser.Xmlschema_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlschema_spec.
    def exitXmlschema_spec(self, ctx:PlSqlParser.Xmlschema_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_table.
    def enterObject_table(self, ctx:PlSqlParser.Object_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_table.
    def exitObject_table(self, ctx:PlSqlParser.Object_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_type.
    def enterObject_type(self, ctx:PlSqlParser.Object_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_type.
    def exitObject_type(self, ctx:PlSqlParser.Object_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#oid_index_clause.
    def enterOid_index_clause(self, ctx:PlSqlParser.Oid_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#oid_index_clause.
    def exitOid_index_clause(self, ctx:PlSqlParser.Oid_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#oid_clause.
    def enterOid_clause(self, ctx:PlSqlParser.Oid_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#oid_clause.
    def exitOid_clause(self, ctx:PlSqlParser.Oid_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_properties.
    def enterObject_properties(self, ctx:PlSqlParser.Object_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_properties.
    def exitObject_properties(self, ctx:PlSqlParser.Object_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_table_substitution.
    def enterObject_table_substitution(self, ctx:PlSqlParser.Object_table_substitutionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_table_substitution.
    def exitObject_table_substitution(self, ctx:PlSqlParser.Object_table_substitutionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relational_table.
    def enterRelational_table(self, ctx:PlSqlParser.Relational_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relational_table.
    def exitRelational_table(self, ctx:PlSqlParser.Relational_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#immutable_table_clauses.
    def enterImmutable_table_clauses(self, ctx:PlSqlParser.Immutable_table_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#immutable_table_clauses.
    def exitImmutable_table_clauses(self, ctx:PlSqlParser.Immutable_table_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#immutable_table_no_drop_clause.
    def enterImmutable_table_no_drop_clause(self, ctx:PlSqlParser.Immutable_table_no_drop_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#immutable_table_no_drop_clause.
    def exitImmutable_table_no_drop_clause(self, ctx:PlSqlParser.Immutable_table_no_drop_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#immutable_table_no_delete_clause.
    def enterImmutable_table_no_delete_clause(self, ctx:PlSqlParser.Immutable_table_no_delete_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#immutable_table_no_delete_clause.
    def exitImmutable_table_no_delete_clause(self, ctx:PlSqlParser.Immutable_table_no_delete_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#blockchain_table_clauses.
    def enterBlockchain_table_clauses(self, ctx:PlSqlParser.Blockchain_table_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#blockchain_table_clauses.
    def exitBlockchain_table_clauses(self, ctx:PlSqlParser.Blockchain_table_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#blockchain_drop_table_clause.
    def enterBlockchain_drop_table_clause(self, ctx:PlSqlParser.Blockchain_drop_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#blockchain_drop_table_clause.
    def exitBlockchain_drop_table_clause(self, ctx:PlSqlParser.Blockchain_drop_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#blockchain_row_retention_clause.
    def enterBlockchain_row_retention_clause(self, ctx:PlSqlParser.Blockchain_row_retention_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#blockchain_row_retention_clause.
    def exitBlockchain_row_retention_clause(self, ctx:PlSqlParser.Blockchain_row_retention_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#blockchain_hash_and_data_format_clause.
    def enterBlockchain_hash_and_data_format_clause(self, ctx:PlSqlParser.Blockchain_hash_and_data_format_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#blockchain_hash_and_data_format_clause.
    def exitBlockchain_hash_and_data_format_clause(self, ctx:PlSqlParser.Blockchain_hash_and_data_format_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collation_name.
    def enterCollation_name(self, ctx:PlSqlParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collation_name.
    def exitCollation_name(self, ctx:PlSqlParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_properties.
    def enterTable_properties(self, ctx:PlSqlParser.Table_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_properties.
    def exitTable_properties(self, ctx:PlSqlParser.Table_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#read_only_clause.
    def enterRead_only_clause(self, ctx:PlSqlParser.Read_only_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#read_only_clause.
    def exitRead_only_clause(self, ctx:PlSqlParser.Read_only_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#indexing_clause.
    def enterIndexing_clause(self, ctx:PlSqlParser.Indexing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#indexing_clause.
    def exitIndexing_clause(self, ctx:PlSqlParser.Indexing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_clustering_clause.
    def enterAttribute_clustering_clause(self, ctx:PlSqlParser.Attribute_clustering_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_clustering_clause.
    def exitAttribute_clustering_clause(self, ctx:PlSqlParser.Attribute_clustering_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#clustering_join.
    def enterClustering_join(self, ctx:PlSqlParser.Clustering_joinContext):
        pass

    # Exit a parse tree produced by PlSqlParser#clustering_join.
    def exitClustering_join(self, ctx:PlSqlParser.Clustering_joinContext):
        pass


    # Enter a parse tree produced by PlSqlParser#clustering_join_item.
    def enterClustering_join_item(self, ctx:PlSqlParser.Clustering_join_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#clustering_join_item.
    def exitClustering_join_item(self, ctx:PlSqlParser.Clustering_join_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#equijoin_condition.
    def enterEquijoin_condition(self, ctx:PlSqlParser.Equijoin_conditionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#equijoin_condition.
    def exitEquijoin_condition(self, ctx:PlSqlParser.Equijoin_conditionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cluster_clause.
    def enterCluster_clause(self, ctx:PlSqlParser.Cluster_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cluster_clause.
    def exitCluster_clause(self, ctx:PlSqlParser.Cluster_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#clustering_columns.
    def enterClustering_columns(self, ctx:PlSqlParser.Clustering_columnsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#clustering_columns.
    def exitClustering_columns(self, ctx:PlSqlParser.Clustering_columnsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#clustering_column_group.
    def enterClustering_column_group(self, ctx:PlSqlParser.Clustering_column_groupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#clustering_column_group.
    def exitClustering_column_group(self, ctx:PlSqlParser.Clustering_column_groupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#yes_no.
    def enterYes_no(self, ctx:PlSqlParser.Yes_noContext):
        pass

    # Exit a parse tree produced by PlSqlParser#yes_no.
    def exitYes_no(self, ctx:PlSqlParser.Yes_noContext):
        pass


    # Enter a parse tree produced by PlSqlParser#zonemap_clause.
    def enterZonemap_clause(self, ctx:PlSqlParser.Zonemap_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#zonemap_clause.
    def exitZonemap_clause(self, ctx:PlSqlParser.Zonemap_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logical_replication_clause.
    def enterLogical_replication_clause(self, ctx:PlSqlParser.Logical_replication_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logical_replication_clause.
    def exitLogical_replication_clause(self, ctx:PlSqlParser.Logical_replication_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_name.
    def enterTable_name(self, ctx:PlSqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_name.
    def exitTable_name(self, ctx:PlSqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relational_property.
    def enterRelational_property(self, ctx:PlSqlParser.Relational_propertyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relational_property.
    def exitRelational_property(self, ctx:PlSqlParser.Relational_propertyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_partitioning_clauses.
    def enterTable_partitioning_clauses(self, ctx:PlSqlParser.Table_partitioning_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_partitioning_clauses.
    def exitTable_partitioning_clauses(self, ctx:PlSqlParser.Table_partitioning_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#range_partitions.
    def enterRange_partitions(self, ctx:PlSqlParser.Range_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#range_partitions.
    def exitRange_partitions(self, ctx:PlSqlParser.Range_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#list_partitions.
    def enterList_partitions(self, ctx:PlSqlParser.List_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#list_partitions.
    def exitList_partitions(self, ctx:PlSqlParser.List_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hash_partitions.
    def enterHash_partitions(self, ctx:PlSqlParser.Hash_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hash_partitions.
    def exitHash_partitions(self, ctx:PlSqlParser.Hash_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#individual_hash_partitions.
    def enterIndividual_hash_partitions(self, ctx:PlSqlParser.Individual_hash_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#individual_hash_partitions.
    def exitIndividual_hash_partitions(self, ctx:PlSqlParser.Individual_hash_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hash_partitions_by_quantity.
    def enterHash_partitions_by_quantity(self, ctx:PlSqlParser.Hash_partitions_by_quantityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hash_partitions_by_quantity.
    def exitHash_partitions_by_quantity(self, ctx:PlSqlParser.Hash_partitions_by_quantityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hash_partition_quantity.
    def enterHash_partition_quantity(self, ctx:PlSqlParser.Hash_partition_quantityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hash_partition_quantity.
    def exitHash_partition_quantity(self, ctx:PlSqlParser.Hash_partition_quantityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#composite_range_partitions.
    def enterComposite_range_partitions(self, ctx:PlSqlParser.Composite_range_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#composite_range_partitions.
    def exitComposite_range_partitions(self, ctx:PlSqlParser.Composite_range_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#composite_list_partitions.
    def enterComposite_list_partitions(self, ctx:PlSqlParser.Composite_list_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#composite_list_partitions.
    def exitComposite_list_partitions(self, ctx:PlSqlParser.Composite_list_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#composite_hash_partitions.
    def enterComposite_hash_partitions(self, ctx:PlSqlParser.Composite_hash_partitionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#composite_hash_partitions.
    def exitComposite_hash_partitions(self, ctx:PlSqlParser.Composite_hash_partitionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_partitioning.
    def enterReference_partitioning(self, ctx:PlSqlParser.Reference_partitioningContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_partitioning.
    def exitReference_partitioning(self, ctx:PlSqlParser.Reference_partitioningContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_partition_desc.
    def enterReference_partition_desc(self, ctx:PlSqlParser.Reference_partition_descContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_partition_desc.
    def exitReference_partition_desc(self, ctx:PlSqlParser.Reference_partition_descContext):
        pass


    # Enter a parse tree produced by PlSqlParser#system_partitioning.
    def enterSystem_partitioning(self, ctx:PlSqlParser.System_partitioningContext):
        pass

    # Exit a parse tree produced by PlSqlParser#system_partitioning.
    def exitSystem_partitioning(self, ctx:PlSqlParser.System_partitioningContext):
        pass


    # Enter a parse tree produced by PlSqlParser#range_partition_desc.
    def enterRange_partition_desc(self, ctx:PlSqlParser.Range_partition_descContext):
        pass

    # Exit a parse tree produced by PlSqlParser#range_partition_desc.
    def exitRange_partition_desc(self, ctx:PlSqlParser.Range_partition_descContext):
        pass


    # Enter a parse tree produced by PlSqlParser#list_partition_desc.
    def enterList_partition_desc(self, ctx:PlSqlParser.List_partition_descContext):
        pass

    # Exit a parse tree produced by PlSqlParser#list_partition_desc.
    def exitList_partition_desc(self, ctx:PlSqlParser.List_partition_descContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_template.
    def enterSubpartition_template(self, ctx:PlSqlParser.Subpartition_templateContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_template.
    def exitSubpartition_template(self, ctx:PlSqlParser.Subpartition_templateContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hash_subpartition_quantity.
    def enterHash_subpartition_quantity(self, ctx:PlSqlParser.Hash_subpartition_quantityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hash_subpartition_quantity.
    def exitHash_subpartition_quantity(self, ctx:PlSqlParser.Hash_subpartition_quantityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_by_range.
    def enterSubpartition_by_range(self, ctx:PlSqlParser.Subpartition_by_rangeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_by_range.
    def exitSubpartition_by_range(self, ctx:PlSqlParser.Subpartition_by_rangeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_by_list.
    def enterSubpartition_by_list(self, ctx:PlSqlParser.Subpartition_by_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_by_list.
    def exitSubpartition_by_list(self, ctx:PlSqlParser.Subpartition_by_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_by_hash.
    def enterSubpartition_by_hash(self, ctx:PlSqlParser.Subpartition_by_hashContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_by_hash.
    def exitSubpartition_by_hash(self, ctx:PlSqlParser.Subpartition_by_hashContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_name.
    def enterSubpartition_name(self, ctx:PlSqlParser.Subpartition_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_name.
    def exitSubpartition_name(self, ctx:PlSqlParser.Subpartition_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#range_subpartition_desc.
    def enterRange_subpartition_desc(self, ctx:PlSqlParser.Range_subpartition_descContext):
        pass

    # Exit a parse tree produced by PlSqlParser#range_subpartition_desc.
    def exitRange_subpartition_desc(self, ctx:PlSqlParser.Range_subpartition_descContext):
        pass


    # Enter a parse tree produced by PlSqlParser#list_subpartition_desc.
    def enterList_subpartition_desc(self, ctx:PlSqlParser.List_subpartition_descContext):
        pass

    # Exit a parse tree produced by PlSqlParser#list_subpartition_desc.
    def exitList_subpartition_desc(self, ctx:PlSqlParser.List_subpartition_descContext):
        pass


    # Enter a parse tree produced by PlSqlParser#individual_hash_subparts.
    def enterIndividual_hash_subparts(self, ctx:PlSqlParser.Individual_hash_subpartsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#individual_hash_subparts.
    def exitIndividual_hash_subparts(self, ctx:PlSqlParser.Individual_hash_subpartsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hash_subparts_by_quantity.
    def enterHash_subparts_by_quantity(self, ctx:PlSqlParser.Hash_subparts_by_quantityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hash_subparts_by_quantity.
    def exitHash_subparts_by_quantity(self, ctx:PlSqlParser.Hash_subparts_by_quantityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#range_values_clause.
    def enterRange_values_clause(self, ctx:PlSqlParser.Range_values_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#range_values_clause.
    def exitRange_values_clause(self, ctx:PlSqlParser.Range_values_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#range_values_list.
    def enterRange_values_list(self, ctx:PlSqlParser.Range_values_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#range_values_list.
    def exitRange_values_list(self, ctx:PlSqlParser.Range_values_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#list_values_clause.
    def enterList_values_clause(self, ctx:PlSqlParser.List_values_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#list_values_clause.
    def exitList_values_clause(self, ctx:PlSqlParser.List_values_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_partition_description.
    def enterTable_partition_description(self, ctx:PlSqlParser.Table_partition_descriptionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_partition_description.
    def exitTable_partition_description(self, ctx:PlSqlParser.Table_partition_descriptionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partitioning_storage_clause.
    def enterPartitioning_storage_clause(self, ctx:PlSqlParser.Partitioning_storage_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partitioning_storage_clause.
    def exitPartitioning_storage_clause(self, ctx:PlSqlParser.Partitioning_storage_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_partitioning_storage.
    def enterLob_partitioning_storage(self, ctx:PlSqlParser.Lob_partitioning_storageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_partitioning_storage.
    def exitLob_partitioning_storage(self, ctx:PlSqlParser.Lob_partitioning_storageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datatype_null_enable.
    def enterDatatype_null_enable(self, ctx:PlSqlParser.Datatype_null_enableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datatype_null_enable.
    def exitDatatype_null_enable(self, ctx:PlSqlParser.Datatype_null_enableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#size_clause.
    def enterSize_clause(self, ctx:PlSqlParser.Size_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#size_clause.
    def exitSize_clause(self, ctx:PlSqlParser.Size_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_compression.
    def enterTable_compression(self, ctx:PlSqlParser.Table_compressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_compression.
    def exitTable_compression(self, ctx:PlSqlParser.Table_compressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_table_clause.
    def enterInmemory_table_clause(self, ctx:PlSqlParser.Inmemory_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_table_clause.
    def exitInmemory_table_clause(self, ctx:PlSqlParser.Inmemory_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_attributes.
    def enterInmemory_attributes(self, ctx:PlSqlParser.Inmemory_attributesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_attributes.
    def exitInmemory_attributes(self, ctx:PlSqlParser.Inmemory_attributesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_memcompress.
    def enterInmemory_memcompress(self, ctx:PlSqlParser.Inmemory_memcompressContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_memcompress.
    def exitInmemory_memcompress(self, ctx:PlSqlParser.Inmemory_memcompressContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_priority.
    def enterInmemory_priority(self, ctx:PlSqlParser.Inmemory_priorityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_priority.
    def exitInmemory_priority(self, ctx:PlSqlParser.Inmemory_priorityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_distribute.
    def enterInmemory_distribute(self, ctx:PlSqlParser.Inmemory_distributeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_distribute.
    def exitInmemory_distribute(self, ctx:PlSqlParser.Inmemory_distributeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_duplicate.
    def enterInmemory_duplicate(self, ctx:PlSqlParser.Inmemory_duplicateContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_duplicate.
    def exitInmemory_duplicate(self, ctx:PlSqlParser.Inmemory_duplicateContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inmemory_column_clause.
    def enterInmemory_column_clause(self, ctx:PlSqlParser.Inmemory_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inmemory_column_clause.
    def exitInmemory_column_clause(self, ctx:PlSqlParser.Inmemory_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#physical_attributes_clause.
    def enterPhysical_attributes_clause(self, ctx:PlSqlParser.Physical_attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#physical_attributes_clause.
    def exitPhysical_attributes_clause(self, ctx:PlSqlParser.Physical_attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#storage_clause.
    def enterStorage_clause(self, ctx:PlSqlParser.Storage_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#storage_clause.
    def exitStorage_clause(self, ctx:PlSqlParser.Storage_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#deferred_segment_creation.
    def enterDeferred_segment_creation(self, ctx:PlSqlParser.Deferred_segment_creationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#deferred_segment_creation.
    def exitDeferred_segment_creation(self, ctx:PlSqlParser.Deferred_segment_creationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#segment_attributes_clause.
    def enterSegment_attributes_clause(self, ctx:PlSqlParser.Segment_attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#segment_attributes_clause.
    def exitSegment_attributes_clause(self, ctx:PlSqlParser.Segment_attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#physical_properties.
    def enterPhysical_properties(self, ctx:PlSqlParser.Physical_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#physical_properties.
    def exitPhysical_properties(self, ctx:PlSqlParser.Physical_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_clause.
    def enterIlm_clause(self, ctx:PlSqlParser.Ilm_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_clause.
    def exitIlm_clause(self, ctx:PlSqlParser.Ilm_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_policy_clause.
    def enterIlm_policy_clause(self, ctx:PlSqlParser.Ilm_policy_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_policy_clause.
    def exitIlm_policy_clause(self, ctx:PlSqlParser.Ilm_policy_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_compression_policy.
    def enterIlm_compression_policy(self, ctx:PlSqlParser.Ilm_compression_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_compression_policy.
    def exitIlm_compression_policy(self, ctx:PlSqlParser.Ilm_compression_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_tiering_policy.
    def enterIlm_tiering_policy(self, ctx:PlSqlParser.Ilm_tiering_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_tiering_policy.
    def exitIlm_tiering_policy(self, ctx:PlSqlParser.Ilm_tiering_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_after_on.
    def enterIlm_after_on(self, ctx:PlSqlParser.Ilm_after_onContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_after_on.
    def exitIlm_after_on(self, ctx:PlSqlParser.Ilm_after_onContext):
        pass


    # Enter a parse tree produced by PlSqlParser#segment_group.
    def enterSegment_group(self, ctx:PlSqlParser.Segment_groupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#segment_group.
    def exitSegment_group(self, ctx:PlSqlParser.Segment_groupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_inmemory_policy.
    def enterIlm_inmemory_policy(self, ctx:PlSqlParser.Ilm_inmemory_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_inmemory_policy.
    def exitIlm_inmemory_policy(self, ctx:PlSqlParser.Ilm_inmemory_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ilm_time_period.
    def enterIlm_time_period(self, ctx:PlSqlParser.Ilm_time_periodContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ilm_time_period.
    def exitIlm_time_period(self, ctx:PlSqlParser.Ilm_time_periodContext):
        pass


    # Enter a parse tree produced by PlSqlParser#heap_org_table_clause.
    def enterHeap_org_table_clause(self, ctx:PlSqlParser.Heap_org_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#heap_org_table_clause.
    def exitHeap_org_table_clause(self, ctx:PlSqlParser.Heap_org_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#external_table_clause.
    def enterExternal_table_clause(self, ctx:PlSqlParser.External_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#external_table_clause.
    def exitExternal_table_clause(self, ctx:PlSqlParser.External_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#access_driver_type.
    def enterAccess_driver_type(self, ctx:PlSqlParser.Access_driver_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#access_driver_type.
    def exitAccess_driver_type(self, ctx:PlSqlParser.Access_driver_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#external_table_data_props.
    def enterExternal_table_data_props(self, ctx:PlSqlParser.External_table_data_propsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#external_table_data_props.
    def exitExternal_table_data_props(self, ctx:PlSqlParser.External_table_data_propsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#opaque_format_spec.
    def enterOpaque_format_spec(self, ctx:PlSqlParser.Opaque_format_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#opaque_format_spec.
    def exitOpaque_format_spec(self, ctx:PlSqlParser.Opaque_format_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#row_movement_clause.
    def enterRow_movement_clause(self, ctx:PlSqlParser.Row_movement_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#row_movement_clause.
    def exitRow_movement_clause(self, ctx:PlSqlParser.Row_movement_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_archive_clause.
    def enterFlashback_archive_clause(self, ctx:PlSqlParser.Flashback_archive_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_archive_clause.
    def exitFlashback_archive_clause(self, ctx:PlSqlParser.Flashback_archive_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#log_grp.
    def enterLog_grp(self, ctx:PlSqlParser.Log_grpContext):
        pass

    # Exit a parse tree produced by PlSqlParser#log_grp.
    def exitLog_grp(self, ctx:PlSqlParser.Log_grpContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_table_logging.
    def enterSupplemental_table_logging(self, ctx:PlSqlParser.Supplemental_table_loggingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_table_logging.
    def exitSupplemental_table_logging(self, ctx:PlSqlParser.Supplemental_table_loggingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_log_grp_clause.
    def enterSupplemental_log_grp_clause(self, ctx:PlSqlParser.Supplemental_log_grp_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_log_grp_clause.
    def exitSupplemental_log_grp_clause(self, ctx:PlSqlParser.Supplemental_log_grp_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_id_key_clause.
    def enterSupplemental_id_key_clause(self, ctx:PlSqlParser.Supplemental_id_key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_id_key_clause.
    def exitSupplemental_id_key_clause(self, ctx:PlSqlParser.Supplemental_id_key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#allocate_extent_clause.
    def enterAllocate_extent_clause(self, ctx:PlSqlParser.Allocate_extent_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#allocate_extent_clause.
    def exitAllocate_extent_clause(self, ctx:PlSqlParser.Allocate_extent_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#deallocate_unused_clause.
    def enterDeallocate_unused_clause(self, ctx:PlSqlParser.Deallocate_unused_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#deallocate_unused_clause.
    def exitDeallocate_unused_clause(self, ctx:PlSqlParser.Deallocate_unused_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#shrink_clause.
    def enterShrink_clause(self, ctx:PlSqlParser.Shrink_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#shrink_clause.
    def exitShrink_clause(self, ctx:PlSqlParser.Shrink_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#records_per_block_clause.
    def enterRecords_per_block_clause(self, ctx:PlSqlParser.Records_per_block_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#records_per_block_clause.
    def exitRecords_per_block_clause(self, ctx:PlSqlParser.Records_per_block_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#upgrade_table_clause.
    def enterUpgrade_table_clause(self, ctx:PlSqlParser.Upgrade_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#upgrade_table_clause.
    def exitUpgrade_table_clause(self, ctx:PlSqlParser.Upgrade_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#truncate_table.
    def enterTruncate_table(self, ctx:PlSqlParser.Truncate_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#truncate_table.
    def exitTruncate_table(self, ctx:PlSqlParser.Truncate_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_table.
    def enterDrop_table(self, ctx:PlSqlParser.Drop_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_table.
    def exitDrop_table(self, ctx:PlSqlParser.Drop_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_tablespace.
    def enterDrop_tablespace(self, ctx:PlSqlParser.Drop_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_tablespace.
    def exitDrop_tablespace(self, ctx:PlSqlParser.Drop_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_tablespace_set.
    def enterDrop_tablespace_set(self, ctx:PlSqlParser.Drop_tablespace_setContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_tablespace_set.
    def exitDrop_tablespace_set(self, ctx:PlSqlParser.Drop_tablespace_setContext):
        pass


    # Enter a parse tree produced by PlSqlParser#including_contents_clause.
    def enterIncluding_contents_clause(self, ctx:PlSqlParser.Including_contents_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#including_contents_clause.
    def exitIncluding_contents_clause(self, ctx:PlSqlParser.Including_contents_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_view.
    def enterDrop_view(self, ctx:PlSqlParser.Drop_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_view.
    def exitDrop_view(self, ctx:PlSqlParser.Drop_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#comment_on_column.
    def enterComment_on_column(self, ctx:PlSqlParser.Comment_on_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#comment_on_column.
    def exitComment_on_column(self, ctx:PlSqlParser.Comment_on_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#enable_or_disable.
    def enterEnable_or_disable(self, ctx:PlSqlParser.Enable_or_disableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#enable_or_disable.
    def exitEnable_or_disable(self, ctx:PlSqlParser.Enable_or_disableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#allow_or_disallow.
    def enterAllow_or_disallow(self, ctx:PlSqlParser.Allow_or_disallowContext):
        pass

    # Exit a parse tree produced by PlSqlParser#allow_or_disallow.
    def exitAllow_or_disallow(self, ctx:PlSqlParser.Allow_or_disallowContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_synonym.
    def enterAlter_synonym(self, ctx:PlSqlParser.Alter_synonymContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_synonym.
    def exitAlter_synonym(self, ctx:PlSqlParser.Alter_synonymContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_synonym.
    def enterCreate_synonym(self, ctx:PlSqlParser.Create_synonymContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_synonym.
    def exitCreate_synonym(self, ctx:PlSqlParser.Create_synonymContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_synonym.
    def enterDrop_synonym(self, ctx:PlSqlParser.Drop_synonymContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_synonym.
    def exitDrop_synonym(self, ctx:PlSqlParser.Drop_synonymContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_spfile.
    def enterCreate_spfile(self, ctx:PlSqlParser.Create_spfileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_spfile.
    def exitCreate_spfile(self, ctx:PlSqlParser.Create_spfileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#spfile_name.
    def enterSpfile_name(self, ctx:PlSqlParser.Spfile_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#spfile_name.
    def exitSpfile_name(self, ctx:PlSqlParser.Spfile_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pfile_name.
    def enterPfile_name(self, ctx:PlSqlParser.Pfile_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pfile_name.
    def exitPfile_name(self, ctx:PlSqlParser.Pfile_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#comment_on_table.
    def enterComment_on_table(self, ctx:PlSqlParser.Comment_on_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#comment_on_table.
    def exitComment_on_table(self, ctx:PlSqlParser.Comment_on_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#comment_on_materialized.
    def enterComment_on_materialized(self, ctx:PlSqlParser.Comment_on_materializedContext):
        pass

    # Exit a parse tree produced by PlSqlParser#comment_on_materialized.
    def exitComment_on_materialized(self, ctx:PlSqlParser.Comment_on_materializedContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_analytic_view.
    def enterAlter_analytic_view(self, ctx:PlSqlParser.Alter_analytic_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_analytic_view.
    def exitAlter_analytic_view(self, ctx:PlSqlParser.Alter_analytic_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_add_cache_clause.
    def enterAlter_add_cache_clause(self, ctx:PlSqlParser.Alter_add_cache_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_add_cache_clause.
    def exitAlter_add_cache_clause(self, ctx:PlSqlParser.Alter_add_cache_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#levels_item.
    def enterLevels_item(self, ctx:PlSqlParser.Levels_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#levels_item.
    def exitLevels_item(self, ctx:PlSqlParser.Levels_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#measure_list.
    def enterMeasure_list(self, ctx:PlSqlParser.Measure_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#measure_list.
    def exitMeasure_list(self, ctx:PlSqlParser.Measure_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_drop_cache_clause.
    def enterAlter_drop_cache_clause(self, ctx:PlSqlParser.Alter_drop_cache_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_drop_cache_clause.
    def exitAlter_drop_cache_clause(self, ctx:PlSqlParser.Alter_drop_cache_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_attribute_dimension.
    def enterAlter_attribute_dimension(self, ctx:PlSqlParser.Alter_attribute_dimensionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_attribute_dimension.
    def exitAlter_attribute_dimension(self, ctx:PlSqlParser.Alter_attribute_dimensionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_audit_policy.
    def enterAlter_audit_policy(self, ctx:PlSqlParser.Alter_audit_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_audit_policy.
    def exitAlter_audit_policy(self, ctx:PlSqlParser.Alter_audit_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_cluster.
    def enterAlter_cluster(self, ctx:PlSqlParser.Alter_clusterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_cluster.
    def exitAlter_cluster(self, ctx:PlSqlParser.Alter_clusterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_analytic_view.
    def enterDrop_analytic_view(self, ctx:PlSqlParser.Drop_analytic_viewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_analytic_view.
    def exitDrop_analytic_view(self, ctx:PlSqlParser.Drop_analytic_viewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_attribute_dimension.
    def enterDrop_attribute_dimension(self, ctx:PlSqlParser.Drop_attribute_dimensionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_attribute_dimension.
    def exitDrop_attribute_dimension(self, ctx:PlSqlParser.Drop_attribute_dimensionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_audit_policy.
    def enterDrop_audit_policy(self, ctx:PlSqlParser.Drop_audit_policyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_audit_policy.
    def exitDrop_audit_policy(self, ctx:PlSqlParser.Drop_audit_policyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_flashback_archive.
    def enterDrop_flashback_archive(self, ctx:PlSqlParser.Drop_flashback_archiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_flashback_archive.
    def exitDrop_flashback_archive(self, ctx:PlSqlParser.Drop_flashback_archiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_cluster.
    def enterDrop_cluster(self, ctx:PlSqlParser.Drop_clusterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_cluster.
    def exitDrop_cluster(self, ctx:PlSqlParser.Drop_clusterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_context.
    def enterDrop_context(self, ctx:PlSqlParser.Drop_contextContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_context.
    def exitDrop_context(self, ctx:PlSqlParser.Drop_contextContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_directory.
    def enterDrop_directory(self, ctx:PlSqlParser.Drop_directoryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_directory.
    def exitDrop_directory(self, ctx:PlSqlParser.Drop_directoryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_diskgroup.
    def enterDrop_diskgroup(self, ctx:PlSqlParser.Drop_diskgroupContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_diskgroup.
    def exitDrop_diskgroup(self, ctx:PlSqlParser.Drop_diskgroupContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_edition.
    def enterDrop_edition(self, ctx:PlSqlParser.Drop_editionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_edition.
    def exitDrop_edition(self, ctx:PlSqlParser.Drop_editionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#truncate_cluster.
    def enterTruncate_cluster(self, ctx:PlSqlParser.Truncate_clusterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#truncate_cluster.
    def exitTruncate_cluster(self, ctx:PlSqlParser.Truncate_clusterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cache_or_nocache.
    def enterCache_or_nocache(self, ctx:PlSqlParser.Cache_or_nocacheContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cache_or_nocache.
    def exitCache_or_nocache(self, ctx:PlSqlParser.Cache_or_nocacheContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database_name.
    def enterDatabase_name(self, ctx:PlSqlParser.Database_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database_name.
    def exitDatabase_name(self, ctx:PlSqlParser.Database_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_database.
    def enterAlter_database(self, ctx:PlSqlParser.Alter_databaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_database.
    def exitAlter_database(self, ctx:PlSqlParser.Alter_databaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database_clause.
    def enterDatabase_clause(self, ctx:PlSqlParser.Database_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database_clause.
    def exitDatabase_clause(self, ctx:PlSqlParser.Database_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#startup_clauses.
    def enterStartup_clauses(self, ctx:PlSqlParser.Startup_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#startup_clauses.
    def exitStartup_clauses(self, ctx:PlSqlParser.Startup_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#resetlogs_or_noresetlogs.
    def enterResetlogs_or_noresetlogs(self, ctx:PlSqlParser.Resetlogs_or_noresetlogsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#resetlogs_or_noresetlogs.
    def exitResetlogs_or_noresetlogs(self, ctx:PlSqlParser.Resetlogs_or_noresetlogsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#upgrade_or_downgrade.
    def enterUpgrade_or_downgrade(self, ctx:PlSqlParser.Upgrade_or_downgradeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#upgrade_or_downgrade.
    def exitUpgrade_or_downgrade(self, ctx:PlSqlParser.Upgrade_or_downgradeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#recovery_clauses.
    def enterRecovery_clauses(self, ctx:PlSqlParser.Recovery_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#recovery_clauses.
    def exitRecovery_clauses(self, ctx:PlSqlParser.Recovery_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#begin_or_end.
    def enterBegin_or_end(self, ctx:PlSqlParser.Begin_or_endContext):
        pass

    # Exit a parse tree produced by PlSqlParser#begin_or_end.
    def exitBegin_or_end(self, ctx:PlSqlParser.Begin_or_endContext):
        pass


    # Enter a parse tree produced by PlSqlParser#general_recovery.
    def enterGeneral_recovery(self, ctx:PlSqlParser.General_recoveryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#general_recovery.
    def exitGeneral_recovery(self, ctx:PlSqlParser.General_recoveryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#full_database_recovery.
    def enterFull_database_recovery(self, ctx:PlSqlParser.Full_database_recoveryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#full_database_recovery.
    def exitFull_database_recovery(self, ctx:PlSqlParser.Full_database_recoveryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partial_database_recovery.
    def enterPartial_database_recovery(self, ctx:PlSqlParser.Partial_database_recoveryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partial_database_recovery.
    def exitPartial_database_recovery(self, ctx:PlSqlParser.Partial_database_recoveryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partial_database_recovery_10g.
    def enterPartial_database_recovery_10g(self, ctx:PlSqlParser.Partial_database_recovery_10gContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partial_database_recovery_10g.
    def exitPartial_database_recovery_10g(self, ctx:PlSqlParser.Partial_database_recovery_10gContext):
        pass


    # Enter a parse tree produced by PlSqlParser#managed_standby_recovery.
    def enterManaged_standby_recovery(self, ctx:PlSqlParser.Managed_standby_recoveryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#managed_standby_recovery.
    def exitManaged_standby_recovery(self, ctx:PlSqlParser.Managed_standby_recoveryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#db_name.
    def enterDb_name(self, ctx:PlSqlParser.Db_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#db_name.
    def exitDb_name(self, ctx:PlSqlParser.Db_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database_file_clauses.
    def enterDatabase_file_clauses(self, ctx:PlSqlParser.Database_file_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database_file_clauses.
    def exitDatabase_file_clauses(self, ctx:PlSqlParser.Database_file_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_datafile_clause.
    def enterCreate_datafile_clause(self, ctx:PlSqlParser.Create_datafile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_datafile_clause.
    def exitCreate_datafile_clause(self, ctx:PlSqlParser.Create_datafile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_datafile_clause.
    def enterAlter_datafile_clause(self, ctx:PlSqlParser.Alter_datafile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_datafile_clause.
    def exitAlter_datafile_clause(self, ctx:PlSqlParser.Alter_datafile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_tempfile_clause.
    def enterAlter_tempfile_clause(self, ctx:PlSqlParser.Alter_tempfile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_tempfile_clause.
    def exitAlter_tempfile_clause(self, ctx:PlSqlParser.Alter_tempfile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#move_datafile_clause.
    def enterMove_datafile_clause(self, ctx:PlSqlParser.Move_datafile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#move_datafile_clause.
    def exitMove_datafile_clause(self, ctx:PlSqlParser.Move_datafile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logfile_clauses.
    def enterLogfile_clauses(self, ctx:PlSqlParser.Logfile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logfile_clauses.
    def exitLogfile_clauses(self, ctx:PlSqlParser.Logfile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_logfile_clauses.
    def enterAdd_logfile_clauses(self, ctx:PlSqlParser.Add_logfile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_logfile_clauses.
    def exitAdd_logfile_clauses(self, ctx:PlSqlParser.Add_logfile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#group_redo_logfile.
    def enterGroup_redo_logfile(self, ctx:PlSqlParser.Group_redo_logfileContext):
        pass

    # Exit a parse tree produced by PlSqlParser#group_redo_logfile.
    def exitGroup_redo_logfile(self, ctx:PlSqlParser.Group_redo_logfileContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_logfile_clauses.
    def enterDrop_logfile_clauses(self, ctx:PlSqlParser.Drop_logfile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_logfile_clauses.
    def exitDrop_logfile_clauses(self, ctx:PlSqlParser.Drop_logfile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#switch_logfile_clause.
    def enterSwitch_logfile_clause(self, ctx:PlSqlParser.Switch_logfile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#switch_logfile_clause.
    def exitSwitch_logfile_clause(self, ctx:PlSqlParser.Switch_logfile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_db_logging.
    def enterSupplemental_db_logging(self, ctx:PlSqlParser.Supplemental_db_loggingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_db_logging.
    def exitSupplemental_db_logging(self, ctx:PlSqlParser.Supplemental_db_loggingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_or_drop.
    def enterAdd_or_drop(self, ctx:PlSqlParser.Add_or_dropContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_or_drop.
    def exitAdd_or_drop(self, ctx:PlSqlParser.Add_or_dropContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_plsql_clause.
    def enterSupplemental_plsql_clause(self, ctx:PlSqlParser.Supplemental_plsql_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_plsql_clause.
    def exitSupplemental_plsql_clause(self, ctx:PlSqlParser.Supplemental_plsql_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logfile_descriptor.
    def enterLogfile_descriptor(self, ctx:PlSqlParser.Logfile_descriptorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logfile_descriptor.
    def exitLogfile_descriptor(self, ctx:PlSqlParser.Logfile_descriptorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#controlfile_clauses.
    def enterControlfile_clauses(self, ctx:PlSqlParser.Controlfile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#controlfile_clauses.
    def exitControlfile_clauses(self, ctx:PlSqlParser.Controlfile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trace_file_clause.
    def enterTrace_file_clause(self, ctx:PlSqlParser.Trace_file_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trace_file_clause.
    def exitTrace_file_clause(self, ctx:PlSqlParser.Trace_file_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#standby_database_clauses.
    def enterStandby_database_clauses(self, ctx:PlSqlParser.Standby_database_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#standby_database_clauses.
    def exitStandby_database_clauses(self, ctx:PlSqlParser.Standby_database_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#activate_standby_db_clause.
    def enterActivate_standby_db_clause(self, ctx:PlSqlParser.Activate_standby_db_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#activate_standby_db_clause.
    def exitActivate_standby_db_clause(self, ctx:PlSqlParser.Activate_standby_db_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#maximize_standby_db_clause.
    def enterMaximize_standby_db_clause(self, ctx:PlSqlParser.Maximize_standby_db_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#maximize_standby_db_clause.
    def exitMaximize_standby_db_clause(self, ctx:PlSqlParser.Maximize_standby_db_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#register_logfile_clause.
    def enterRegister_logfile_clause(self, ctx:PlSqlParser.Register_logfile_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#register_logfile_clause.
    def exitRegister_logfile_clause(self, ctx:PlSqlParser.Register_logfile_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#commit_switchover_clause.
    def enterCommit_switchover_clause(self, ctx:PlSqlParser.Commit_switchover_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#commit_switchover_clause.
    def exitCommit_switchover_clause(self, ctx:PlSqlParser.Commit_switchover_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#start_standby_clause.
    def enterStart_standby_clause(self, ctx:PlSqlParser.Start_standby_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#start_standby_clause.
    def exitStart_standby_clause(self, ctx:PlSqlParser.Start_standby_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#stop_standby_clause.
    def enterStop_standby_clause(self, ctx:PlSqlParser.Stop_standby_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#stop_standby_clause.
    def exitStop_standby_clause(self, ctx:PlSqlParser.Stop_standby_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#convert_database_clause.
    def enterConvert_database_clause(self, ctx:PlSqlParser.Convert_database_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#convert_database_clause.
    def exitConvert_database_clause(self, ctx:PlSqlParser.Convert_database_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_settings_clause.
    def enterDefault_settings_clause(self, ctx:PlSqlParser.Default_settings_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_settings_clause.
    def exitDefault_settings_clause(self, ctx:PlSqlParser.Default_settings_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_time_zone_clause.
    def enterSet_time_zone_clause(self, ctx:PlSqlParser.Set_time_zone_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_time_zone_clause.
    def exitSet_time_zone_clause(self, ctx:PlSqlParser.Set_time_zone_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#instance_clauses.
    def enterInstance_clauses(self, ctx:PlSqlParser.Instance_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#instance_clauses.
    def exitInstance_clauses(self, ctx:PlSqlParser.Instance_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#security_clause.
    def enterSecurity_clause(self, ctx:PlSqlParser.Security_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#security_clause.
    def exitSecurity_clause(self, ctx:PlSqlParser.Security_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#domain.
    def enterDomain(self, ctx:PlSqlParser.DomainContext):
        pass

    # Exit a parse tree produced by PlSqlParser#domain.
    def exitDomain(self, ctx:PlSqlParser.DomainContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database.
    def enterDatabase(self, ctx:PlSqlParser.DatabaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database.
    def exitDatabase(self, ctx:PlSqlParser.DatabaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#edition_name.
    def enterEdition_name(self, ctx:PlSqlParser.Edition_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#edition_name.
    def exitEdition_name(self, ctx:PlSqlParser.Edition_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filenumber.
    def enterFilenumber(self, ctx:PlSqlParser.FilenumberContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filenumber.
    def exitFilenumber(self, ctx:PlSqlParser.FilenumberContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filename.
    def enterFilename(self, ctx:PlSqlParser.FilenameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filename.
    def exitFilename(self, ctx:PlSqlParser.FilenameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#prepare_clause.
    def enterPrepare_clause(self, ctx:PlSqlParser.Prepare_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#prepare_clause.
    def exitPrepare_clause(self, ctx:PlSqlParser.Prepare_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_mirror_clause.
    def enterDrop_mirror_clause(self, ctx:PlSqlParser.Drop_mirror_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_mirror_clause.
    def exitDrop_mirror_clause(self, ctx:PlSqlParser.Drop_mirror_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lost_write_protection.
    def enterLost_write_protection(self, ctx:PlSqlParser.Lost_write_protectionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lost_write_protection.
    def exitLost_write_protection(self, ctx:PlSqlParser.Lost_write_protectionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cdb_fleet_clauses.
    def enterCdb_fleet_clauses(self, ctx:PlSqlParser.Cdb_fleet_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cdb_fleet_clauses.
    def exitCdb_fleet_clauses(self, ctx:PlSqlParser.Cdb_fleet_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lead_cdb_clause.
    def enterLead_cdb_clause(self, ctx:PlSqlParser.Lead_cdb_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lead_cdb_clause.
    def exitLead_cdb_clause(self, ctx:PlSqlParser.Lead_cdb_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lead_cdb_uri_clause.
    def enterLead_cdb_uri_clause(self, ctx:PlSqlParser.Lead_cdb_uri_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lead_cdb_uri_clause.
    def exitLead_cdb_uri_clause(self, ctx:PlSqlParser.Lead_cdb_uri_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#property_clauses.
    def enterProperty_clauses(self, ctx:PlSqlParser.Property_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#property_clauses.
    def exitProperty_clauses(self, ctx:PlSqlParser.Property_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#replay_upgrade_clauses.
    def enterReplay_upgrade_clauses(self, ctx:PlSqlParser.Replay_upgrade_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#replay_upgrade_clauses.
    def exitReplay_upgrade_clauses(self, ctx:PlSqlParser.Replay_upgrade_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_database_link.
    def enterAlter_database_link(self, ctx:PlSqlParser.Alter_database_linkContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_database_link.
    def exitAlter_database_link(self, ctx:PlSqlParser.Alter_database_linkContext):
        pass


    # Enter a parse tree produced by PlSqlParser#password_value.
    def enterPassword_value(self, ctx:PlSqlParser.Password_valueContext):
        pass

    # Exit a parse tree produced by PlSqlParser#password_value.
    def exitPassword_value(self, ctx:PlSqlParser.Password_valueContext):
        pass


    # Enter a parse tree produced by PlSqlParser#link_authentication.
    def enterLink_authentication(self, ctx:PlSqlParser.Link_authenticationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#link_authentication.
    def exitLink_authentication(self, ctx:PlSqlParser.Link_authenticationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_database.
    def enterCreate_database(self, ctx:PlSqlParser.Create_databaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_database.
    def exitCreate_database(self, ctx:PlSqlParser.Create_databaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database_logging_clauses.
    def enterDatabase_logging_clauses(self, ctx:PlSqlParser.Database_logging_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database_logging_clauses.
    def exitDatabase_logging_clauses(self, ctx:PlSqlParser.Database_logging_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#database_logging_sub_clause.
    def enterDatabase_logging_sub_clause(self, ctx:PlSqlParser.Database_logging_sub_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#database_logging_sub_clause.
    def exitDatabase_logging_sub_clause(self, ctx:PlSqlParser.Database_logging_sub_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_clauses.
    def enterTablespace_clauses(self, ctx:PlSqlParser.Tablespace_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_clauses.
    def exitTablespace_clauses(self, ctx:PlSqlParser.Tablespace_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#enable_pluggable_database.
    def enterEnable_pluggable_database(self, ctx:PlSqlParser.Enable_pluggable_databaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#enable_pluggable_database.
    def exitEnable_pluggable_database(self, ctx:PlSqlParser.Enable_pluggable_databaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#file_name_convert.
    def enterFile_name_convert(self, ctx:PlSqlParser.File_name_convertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#file_name_convert.
    def exitFile_name_convert(self, ctx:PlSqlParser.File_name_convertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filename_convert_sub_clause.
    def enterFilename_convert_sub_clause(self, ctx:PlSqlParser.Filename_convert_sub_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filename_convert_sub_clause.
    def exitFilename_convert_sub_clause(self, ctx:PlSqlParser.Filename_convert_sub_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace_datafile_clauses.
    def enterTablespace_datafile_clauses(self, ctx:PlSqlParser.Tablespace_datafile_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace_datafile_clauses.
    def exitTablespace_datafile_clauses(self, ctx:PlSqlParser.Tablespace_datafile_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#undo_mode_clause.
    def enterUndo_mode_clause(self, ctx:PlSqlParser.Undo_mode_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#undo_mode_clause.
    def exitUndo_mode_clause(self, ctx:PlSqlParser.Undo_mode_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_tablespace.
    def enterDefault_tablespace(self, ctx:PlSqlParser.Default_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_tablespace.
    def exitDefault_tablespace(self, ctx:PlSqlParser.Default_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_temp_tablespace.
    def enterDefault_temp_tablespace(self, ctx:PlSqlParser.Default_temp_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_temp_tablespace.
    def exitDefault_temp_tablespace(self, ctx:PlSqlParser.Default_temp_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#undo_tablespace.
    def enterUndo_tablespace(self, ctx:PlSqlParser.Undo_tablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#undo_tablespace.
    def exitUndo_tablespace(self, ctx:PlSqlParser.Undo_tablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_database.
    def enterDrop_database(self, ctx:PlSqlParser.Drop_databaseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_database.
    def exitDrop_database(self, ctx:PlSqlParser.Drop_databaseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#create_database_link.
    def enterCreate_database_link(self, ctx:PlSqlParser.Create_database_linkContext):
        pass

    # Exit a parse tree produced by PlSqlParser#create_database_link.
    def exitCreate_database_link(self, ctx:PlSqlParser.Create_database_linkContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_database_link.
    def enterDrop_database_link(self, ctx:PlSqlParser.Drop_database_linkContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_database_link.
    def exitDrop_database_link(self, ctx:PlSqlParser.Drop_database_linkContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_tablespace_set.
    def enterAlter_tablespace_set(self, ctx:PlSqlParser.Alter_tablespace_setContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_tablespace_set.
    def exitAlter_tablespace_set(self, ctx:PlSqlParser.Alter_tablespace_setContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_tablespace_attrs.
    def enterAlter_tablespace_attrs(self, ctx:PlSqlParser.Alter_tablespace_attrsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_tablespace_attrs.
    def exitAlter_tablespace_attrs(self, ctx:PlSqlParser.Alter_tablespace_attrsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_tablespace_encryption.
    def enterAlter_tablespace_encryption(self, ctx:PlSqlParser.Alter_tablespace_encryptionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_tablespace_encryption.
    def exitAlter_tablespace_encryption(self, ctx:PlSqlParser.Alter_tablespace_encryptionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ts_file_name_convert.
    def enterTs_file_name_convert(self, ctx:PlSqlParser.Ts_file_name_convertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ts_file_name_convert.
    def exitTs_file_name_convert(self, ctx:PlSqlParser.Ts_file_name_convertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_role.
    def enterAlter_role(self, ctx:PlSqlParser.Alter_roleContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_role.
    def exitAlter_role(self, ctx:PlSqlParser.Alter_roleContext):
        pass


    # Enter a parse tree produced by PlSqlParser#role_identified_clause.
    def enterRole_identified_clause(self, ctx:PlSqlParser.Role_identified_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#role_identified_clause.
    def exitRole_identified_clause(self, ctx:PlSqlParser.Role_identified_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_table.
    def enterAlter_table(self, ctx:PlSqlParser.Alter_tableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_table.
    def exitAlter_table(self, ctx:PlSqlParser.Alter_tableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#memoptimize_read_write_clause.
    def enterMemoptimize_read_write_clause(self, ctx:PlSqlParser.Memoptimize_read_write_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#memoptimize_read_write_clause.
    def exitMemoptimize_read_write_clause(self, ctx:PlSqlParser.Memoptimize_read_write_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_table_properties.
    def enterAlter_table_properties(self, ctx:PlSqlParser.Alter_table_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_table_properties.
    def exitAlter_table_properties(self, ctx:PlSqlParser.Alter_table_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_table_partitioning.
    def enterAlter_table_partitioning(self, ctx:PlSqlParser.Alter_table_partitioningContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_table_partitioning.
    def exitAlter_table_partitioning(self, ctx:PlSqlParser.Alter_table_partitioningContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_table_partition.
    def enterAdd_table_partition(self, ctx:PlSqlParser.Add_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_table_partition.
    def exitAdd_table_partition(self, ctx:PlSqlParser.Add_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_table_partition.
    def enterDrop_table_partition(self, ctx:PlSqlParser.Drop_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_table_partition.
    def exitDrop_table_partition(self, ctx:PlSqlParser.Drop_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_table_partition.
    def enterMerge_table_partition(self, ctx:PlSqlParser.Merge_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_table_partition.
    def exitMerge_table_partition(self, ctx:PlSqlParser.Merge_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_table_partition.
    def enterModify_table_partition(self, ctx:PlSqlParser.Modify_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_table_partition.
    def exitModify_table_partition(self, ctx:PlSqlParser.Modify_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#split_table_partition.
    def enterSplit_table_partition(self, ctx:PlSqlParser.Split_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#split_table_partition.
    def exitSplit_table_partition(self, ctx:PlSqlParser.Split_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#truncate_table_partition.
    def enterTruncate_table_partition(self, ctx:PlSqlParser.Truncate_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#truncate_table_partition.
    def exitTruncate_table_partition(self, ctx:PlSqlParser.Truncate_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exchange_table_partition.
    def enterExchange_table_partition(self, ctx:PlSqlParser.Exchange_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exchange_table_partition.
    def exitExchange_table_partition(self, ctx:PlSqlParser.Exchange_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#coalesce_table_partition.
    def enterCoalesce_table_partition(self, ctx:PlSqlParser.Coalesce_table_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#coalesce_table_partition.
    def exitCoalesce_table_partition(self, ctx:PlSqlParser.Coalesce_table_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_interval_partition.
    def enterAlter_interval_partition(self, ctx:PlSqlParser.Alter_interval_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_interval_partition.
    def exitAlter_interval_partition(self, ctx:PlSqlParser.Alter_interval_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_extended_names.
    def enterPartition_extended_names(self, ctx:PlSqlParser.Partition_extended_namesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_extended_names.
    def exitPartition_extended_names(self, ctx:PlSqlParser.Partition_extended_namesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subpartition_extended_names.
    def enterSubpartition_extended_names(self, ctx:PlSqlParser.Subpartition_extended_namesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subpartition_extended_names.
    def exitSubpartition_extended_names(self, ctx:PlSqlParser.Subpartition_extended_namesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_table_properties_1.
    def enterAlter_table_properties_1(self, ctx:PlSqlParser.Alter_table_properties_1Context):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_table_properties_1.
    def exitAlter_table_properties_1(self, ctx:PlSqlParser.Alter_table_properties_1Context):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_iot_clauses.
    def enterAlter_iot_clauses(self, ctx:PlSqlParser.Alter_iot_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_iot_clauses.
    def exitAlter_iot_clauses(self, ctx:PlSqlParser.Alter_iot_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_mapping_table_clause.
    def enterAlter_mapping_table_clause(self, ctx:PlSqlParser.Alter_mapping_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_mapping_table_clause.
    def exitAlter_mapping_table_clause(self, ctx:PlSqlParser.Alter_mapping_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_overflow_clause.
    def enterAlter_overflow_clause(self, ctx:PlSqlParser.Alter_overflow_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_overflow_clause.
    def exitAlter_overflow_clause(self, ctx:PlSqlParser.Alter_overflow_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_overflow_clause.
    def enterAdd_overflow_clause(self, ctx:PlSqlParser.Add_overflow_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_overflow_clause.
    def exitAdd_overflow_clause(self, ctx:PlSqlParser.Add_overflow_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_index_clauses.
    def enterUpdate_index_clauses(self, ctx:PlSqlParser.Update_index_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_index_clauses.
    def exitUpdate_index_clauses(self, ctx:PlSqlParser.Update_index_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_global_index_clause.
    def enterUpdate_global_index_clause(self, ctx:PlSqlParser.Update_global_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_global_index_clause.
    def exitUpdate_global_index_clause(self, ctx:PlSqlParser.Update_global_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_all_indexes_clause.
    def enterUpdate_all_indexes_clause(self, ctx:PlSqlParser.Update_all_indexes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_all_indexes_clause.
    def exitUpdate_all_indexes_clause(self, ctx:PlSqlParser.Update_all_indexes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_all_indexes_index_clause.
    def enterUpdate_all_indexes_index_clause(self, ctx:PlSqlParser.Update_all_indexes_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_all_indexes_index_clause.
    def exitUpdate_all_indexes_index_clause(self, ctx:PlSqlParser.Update_all_indexes_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_index_partition.
    def enterUpdate_index_partition(self, ctx:PlSqlParser.Update_index_partitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_index_partition.
    def exitUpdate_index_partition(self, ctx:PlSqlParser.Update_index_partitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_index_subpartition.
    def enterUpdate_index_subpartition(self, ctx:PlSqlParser.Update_index_subpartitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_index_subpartition.
    def exitUpdate_index_subpartition(self, ctx:PlSqlParser.Update_index_subpartitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#enable_disable_clause.
    def enterEnable_disable_clause(self, ctx:PlSqlParser.Enable_disable_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#enable_disable_clause.
    def exitEnable_disable_clause(self, ctx:PlSqlParser.Enable_disable_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_index_clause.
    def enterUsing_index_clause(self, ctx:PlSqlParser.Using_index_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_index_clause.
    def exitUsing_index_clause(self, ctx:PlSqlParser.Using_index_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_attributes.
    def enterIndex_attributes(self, ctx:PlSqlParser.Index_attributesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_attributes.
    def exitIndex_attributes(self, ctx:PlSqlParser.Index_attributesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sort_or_nosort.
    def enterSort_or_nosort(self, ctx:PlSqlParser.Sort_or_nosortContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sort_or_nosort.
    def exitSort_or_nosort(self, ctx:PlSqlParser.Sort_or_nosortContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exceptions_clause.
    def enterExceptions_clause(self, ctx:PlSqlParser.Exceptions_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exceptions_clause.
    def exitExceptions_clause(self, ctx:PlSqlParser.Exceptions_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#move_table_clause.
    def enterMove_table_clause(self, ctx:PlSqlParser.Move_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#move_table_clause.
    def exitMove_table_clause(self, ctx:PlSqlParser.Move_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_org_table_clause.
    def enterIndex_org_table_clause(self, ctx:PlSqlParser.Index_org_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_org_table_clause.
    def exitIndex_org_table_clause(self, ctx:PlSqlParser.Index_org_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#mapping_table_clause.
    def enterMapping_table_clause(self, ctx:PlSqlParser.Mapping_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#mapping_table_clause.
    def exitMapping_table_clause(self, ctx:PlSqlParser.Mapping_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#key_compression.
    def enterKey_compression(self, ctx:PlSqlParser.Key_compressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#key_compression.
    def exitKey_compression(self, ctx:PlSqlParser.Key_compressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_org_overflow_clause.
    def enterIndex_org_overflow_clause(self, ctx:PlSqlParser.Index_org_overflow_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_org_overflow_clause.
    def exitIndex_org_overflow_clause(self, ctx:PlSqlParser.Index_org_overflow_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_clauses.
    def enterColumn_clauses(self, ctx:PlSqlParser.Column_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_clauses.
    def exitColumn_clauses(self, ctx:PlSqlParser.Column_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_collection_retrieval.
    def enterModify_collection_retrieval(self, ctx:PlSqlParser.Modify_collection_retrievalContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_collection_retrieval.
    def exitModify_collection_retrieval(self, ctx:PlSqlParser.Modify_collection_retrievalContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collection_item.
    def enterCollection_item(self, ctx:PlSqlParser.Collection_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collection_item.
    def exitCollection_item(self, ctx:PlSqlParser.Collection_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rename_column_clause.
    def enterRename_column_clause(self, ctx:PlSqlParser.Rename_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rename_column_clause.
    def exitRename_column_clause(self, ctx:PlSqlParser.Rename_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#old_column_name.
    def enterOld_column_name(self, ctx:PlSqlParser.Old_column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#old_column_name.
    def exitOld_column_name(self, ctx:PlSqlParser.Old_column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_column_name.
    def enterNew_column_name(self, ctx:PlSqlParser.New_column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_column_name.
    def exitNew_column_name(self, ctx:PlSqlParser.New_column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_modify_drop_column_clauses.
    def enterAdd_modify_drop_column_clauses(self, ctx:PlSqlParser.Add_modify_drop_column_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_modify_drop_column_clauses.
    def exitAdd_modify_drop_column_clauses(self, ctx:PlSqlParser.Add_modify_drop_column_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_column_clause.
    def enterDrop_column_clause(self, ctx:PlSqlParser.Drop_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_column_clause.
    def exitDrop_column_clause(self, ctx:PlSqlParser.Drop_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_column_clauses.
    def enterModify_column_clauses(self, ctx:PlSqlParser.Modify_column_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_column_clauses.
    def exitModify_column_clauses(self, ctx:PlSqlParser.Modify_column_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_col_properties.
    def enterModify_col_properties(self, ctx:PlSqlParser.Modify_col_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_col_properties.
    def exitModify_col_properties(self, ctx:PlSqlParser.Modify_col_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_col_visibility.
    def enterModify_col_visibility(self, ctx:PlSqlParser.Modify_col_visibilityContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_col_visibility.
    def exitModify_col_visibility(self, ctx:PlSqlParser.Modify_col_visibilityContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_col_substitutable.
    def enterModify_col_substitutable(self, ctx:PlSqlParser.Modify_col_substitutableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_col_substitutable.
    def exitModify_col_substitutable(self, ctx:PlSqlParser.Modify_col_substitutableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_column_clause.
    def enterAdd_column_clause(self, ctx:PlSqlParser.Add_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_column_clause.
    def exitAdd_column_clause(self, ctx:PlSqlParser.Add_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#alter_varray_col_properties.
    def enterAlter_varray_col_properties(self, ctx:PlSqlParser.Alter_varray_col_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#alter_varray_col_properties.
    def exitAlter_varray_col_properties(self, ctx:PlSqlParser.Alter_varray_col_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#varray_col_properties.
    def enterVarray_col_properties(self, ctx:PlSqlParser.Varray_col_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#varray_col_properties.
    def exitVarray_col_properties(self, ctx:PlSqlParser.Varray_col_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#varray_storage_clause.
    def enterVarray_storage_clause(self, ctx:PlSqlParser.Varray_storage_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#varray_storage_clause.
    def exitVarray_storage_clause(self, ctx:PlSqlParser.Varray_storage_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_segname.
    def enterLob_segname(self, ctx:PlSqlParser.Lob_segnameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_segname.
    def exitLob_segname(self, ctx:PlSqlParser.Lob_segnameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_item.
    def enterLob_item(self, ctx:PlSqlParser.Lob_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_item.
    def exitLob_item(self, ctx:PlSqlParser.Lob_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_storage_parameters.
    def enterLob_storage_parameters(self, ctx:PlSqlParser.Lob_storage_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_storage_parameters.
    def exitLob_storage_parameters(self, ctx:PlSqlParser.Lob_storage_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_storage_clause.
    def enterLob_storage_clause(self, ctx:PlSqlParser.Lob_storage_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_storage_clause.
    def exitLob_storage_clause(self, ctx:PlSqlParser.Lob_storage_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_lob_storage_clause.
    def enterModify_lob_storage_clause(self, ctx:PlSqlParser.Modify_lob_storage_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_lob_storage_clause.
    def exitModify_lob_storage_clause(self, ctx:PlSqlParser.Modify_lob_storage_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#modify_lob_parameters.
    def enterModify_lob_parameters(self, ctx:PlSqlParser.Modify_lob_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#modify_lob_parameters.
    def exitModify_lob_parameters(self, ctx:PlSqlParser.Modify_lob_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_parameters.
    def enterLob_parameters(self, ctx:PlSqlParser.Lob_parametersContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_parameters.
    def exitLob_parameters(self, ctx:PlSqlParser.Lob_parametersContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_deduplicate_clause.
    def enterLob_deduplicate_clause(self, ctx:PlSqlParser.Lob_deduplicate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_deduplicate_clause.
    def exitLob_deduplicate_clause(self, ctx:PlSqlParser.Lob_deduplicate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_compression_clause.
    def enterLob_compression_clause(self, ctx:PlSqlParser.Lob_compression_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_compression_clause.
    def exitLob_compression_clause(self, ctx:PlSqlParser.Lob_compression_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_retention_clause.
    def enterLob_retention_clause(self, ctx:PlSqlParser.Lob_retention_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_retention_clause.
    def exitLob_retention_clause(self, ctx:PlSqlParser.Lob_retention_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#encryption_spec.
    def enterEncryption_spec(self, ctx:PlSqlParser.Encryption_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#encryption_spec.
    def exitEncryption_spec(self, ctx:PlSqlParser.Encryption_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tablespace.
    def enterTablespace(self, ctx:PlSqlParser.TablespaceContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tablespace.
    def exitTablespace(self, ctx:PlSqlParser.TablespaceContext):
        pass


    # Enter a parse tree produced by PlSqlParser#varray_item.
    def enterVarray_item(self, ctx:PlSqlParser.Varray_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#varray_item.
    def exitVarray_item(self, ctx:PlSqlParser.Varray_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_properties.
    def enterColumn_properties(self, ctx:PlSqlParser.Column_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_properties.
    def exitColumn_properties(self, ctx:PlSqlParser.Column_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lob_partition_storage.
    def enterLob_partition_storage(self, ctx:PlSqlParser.Lob_partition_storageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lob_partition_storage.
    def exitLob_partition_storage(self, ctx:PlSqlParser.Lob_partition_storageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#period_definition.
    def enterPeriod_definition(self, ctx:PlSqlParser.Period_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#period_definition.
    def exitPeriod_definition(self, ctx:PlSqlParser.Period_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#start_time_column.
    def enterStart_time_column(self, ctx:PlSqlParser.Start_time_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#start_time_column.
    def exitStart_time_column(self, ctx:PlSqlParser.Start_time_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#end_time_column.
    def enterEnd_time_column(self, ctx:PlSqlParser.End_time_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#end_time_column.
    def exitEnd_time_column(self, ctx:PlSqlParser.End_time_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_definition.
    def enterColumn_definition(self, ctx:PlSqlParser.Column_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_definition.
    def exitColumn_definition(self, ctx:PlSqlParser.Column_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_collation_name.
    def enterColumn_collation_name(self, ctx:PlSqlParser.Column_collation_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_collation_name.
    def exitColumn_collation_name(self, ctx:PlSqlParser.Column_collation_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identity_clause.
    def enterIdentity_clause(self, ctx:PlSqlParser.Identity_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identity_clause.
    def exitIdentity_clause(self, ctx:PlSqlParser.Identity_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identity_options_parentheses.
    def enterIdentity_options_parentheses(self, ctx:PlSqlParser.Identity_options_parenthesesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identity_options_parentheses.
    def exitIdentity_options_parentheses(self, ctx:PlSqlParser.Identity_options_parenthesesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identity_options.
    def enterIdentity_options(self, ctx:PlSqlParser.Identity_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identity_options.
    def exitIdentity_options(self, ctx:PlSqlParser.Identity_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#virtual_column_definition.
    def enterVirtual_column_definition(self, ctx:PlSqlParser.Virtual_column_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#virtual_column_definition.
    def exitVirtual_column_definition(self, ctx:PlSqlParser.Virtual_column_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#autogenerated_sequence_definition.
    def enterAutogenerated_sequence_definition(self, ctx:PlSqlParser.Autogenerated_sequence_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#autogenerated_sequence_definition.
    def exitAutogenerated_sequence_definition(self, ctx:PlSqlParser.Autogenerated_sequence_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#evaluation_edition_clause.
    def enterEvaluation_edition_clause(self, ctx:PlSqlParser.Evaluation_edition_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#evaluation_edition_clause.
    def exitEvaluation_edition_clause(self, ctx:PlSqlParser.Evaluation_edition_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#out_of_line_part_storage.
    def enterOut_of_line_part_storage(self, ctx:PlSqlParser.Out_of_line_part_storageContext):
        pass

    # Exit a parse tree produced by PlSqlParser#out_of_line_part_storage.
    def exitOut_of_line_part_storage(self, ctx:PlSqlParser.Out_of_line_part_storageContext):
        pass


    # Enter a parse tree produced by PlSqlParser#nested_table_col_properties.
    def enterNested_table_col_properties(self, ctx:PlSqlParser.Nested_table_col_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#nested_table_col_properties.
    def exitNested_table_col_properties(self, ctx:PlSqlParser.Nested_table_col_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#nested_item.
    def enterNested_item(self, ctx:PlSqlParser.Nested_itemContext):
        pass

    # Exit a parse tree produced by PlSqlParser#nested_item.
    def exitNested_item(self, ctx:PlSqlParser.Nested_itemContext):
        pass


    # Enter a parse tree produced by PlSqlParser#substitutable_column_clause.
    def enterSubstitutable_column_clause(self, ctx:PlSqlParser.Substitutable_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#substitutable_column_clause.
    def exitSubstitutable_column_clause(self, ctx:PlSqlParser.Substitutable_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_name.
    def enterPartition_name(self, ctx:PlSqlParser.Partition_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_name.
    def exitPartition_name(self, ctx:PlSqlParser.Partition_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#supplemental_logging_props.
    def enterSupplemental_logging_props(self, ctx:PlSqlParser.Supplemental_logging_propsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#supplemental_logging_props.
    def exitSupplemental_logging_props(self, ctx:PlSqlParser.Supplemental_logging_propsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_or_attribute.
    def enterColumn_or_attribute(self, ctx:PlSqlParser.Column_or_attributeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_or_attribute.
    def exitColumn_or_attribute(self, ctx:PlSqlParser.Column_or_attributeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_type_col_properties.
    def enterObject_type_col_properties(self, ctx:PlSqlParser.Object_type_col_propertiesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_type_col_properties.
    def exitObject_type_col_properties(self, ctx:PlSqlParser.Object_type_col_propertiesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constraint_clauses.
    def enterConstraint_clauses(self, ctx:PlSqlParser.Constraint_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constraint_clauses.
    def exitConstraint_clauses(self, ctx:PlSqlParser.Constraint_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#old_constraint_name.
    def enterOld_constraint_name(self, ctx:PlSqlParser.Old_constraint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#old_constraint_name.
    def exitOld_constraint_name(self, ctx:PlSqlParser.Old_constraint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#new_constraint_name.
    def enterNew_constraint_name(self, ctx:PlSqlParser.New_constraint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#new_constraint_name.
    def exitNew_constraint_name(self, ctx:PlSqlParser.New_constraint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_constraint_clause.
    def enterDrop_constraint_clause(self, ctx:PlSqlParser.Drop_constraint_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_constraint_clause.
    def exitDrop_constraint_clause(self, ctx:PlSqlParser.Drop_constraint_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_constraint.
    def enterAdd_constraint(self, ctx:PlSqlParser.Add_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_constraint.
    def exitAdd_constraint(self, ctx:PlSqlParser.Add_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_constraint_clause.
    def enterAdd_constraint_clause(self, ctx:PlSqlParser.Add_constraint_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_constraint_clause.
    def exitAdd_constraint_clause(self, ctx:PlSqlParser.Add_constraint_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#check_constraint.
    def enterCheck_constraint(self, ctx:PlSqlParser.Check_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#check_constraint.
    def exitCheck_constraint(self, ctx:PlSqlParser.Check_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#drop_constraint.
    def enterDrop_constraint(self, ctx:PlSqlParser.Drop_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#drop_constraint.
    def exitDrop_constraint(self, ctx:PlSqlParser.Drop_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#enable_constraint.
    def enterEnable_constraint(self, ctx:PlSqlParser.Enable_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#enable_constraint.
    def exitEnable_constraint(self, ctx:PlSqlParser.Enable_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#disable_constraint.
    def enterDisable_constraint(self, ctx:PlSqlParser.Disable_constraintContext):
        pass

    # Exit a parse tree produced by PlSqlParser#disable_constraint.
    def exitDisable_constraint(self, ctx:PlSqlParser.Disable_constraintContext):
        pass


    # Enter a parse tree produced by PlSqlParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx:PlSqlParser.Foreign_key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx:PlSqlParser.Foreign_key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#references_clause.
    def enterReferences_clause(self, ctx:PlSqlParser.References_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#references_clause.
    def exitReferences_clause(self, ctx:PlSqlParser.References_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#on_delete_clause.
    def enterOn_delete_clause(self, ctx:PlSqlParser.On_delete_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#on_delete_clause.
    def exitOn_delete_clause(self, ctx:PlSqlParser.On_delete_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unique_key_clause.
    def enterUnique_key_clause(self, ctx:PlSqlParser.Unique_key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unique_key_clause.
    def exitUnique_key_clause(self, ctx:PlSqlParser.Unique_key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#primary_key_clause.
    def enterPrimary_key_clause(self, ctx:PlSqlParser.Primary_key_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#primary_key_clause.
    def exitPrimary_key_clause(self, ctx:PlSqlParser.Primary_key_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#anonymous_block.
    def enterAnonymous_block(self, ctx:PlSqlParser.Anonymous_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#anonymous_block.
    def exitAnonymous_block(self, ctx:PlSqlParser.Anonymous_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#invoker_rights_clause.
    def enterInvoker_rights_clause(self, ctx:PlSqlParser.Invoker_rights_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#invoker_rights_clause.
    def exitInvoker_rights_clause(self, ctx:PlSqlParser.Invoker_rights_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#call_spec.
    def enterCall_spec(self, ctx:PlSqlParser.Call_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#call_spec.
    def exitCall_spec(self, ctx:PlSqlParser.Call_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#java_spec.
    def enterJava_spec(self, ctx:PlSqlParser.Java_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#java_spec.
    def exitJava_spec(self, ctx:PlSqlParser.Java_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_spec.
    def enterC_spec(self, ctx:PlSqlParser.C_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_spec.
    def exitC_spec(self, ctx:PlSqlParser.C_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_agent_in_clause.
    def enterC_agent_in_clause(self, ctx:PlSqlParser.C_agent_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_agent_in_clause.
    def exitC_agent_in_clause(self, ctx:PlSqlParser.C_agent_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_parameters_clause.
    def enterC_parameters_clause(self, ctx:PlSqlParser.C_parameters_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_parameters_clause.
    def exitC_parameters_clause(self, ctx:PlSqlParser.C_parameters_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_external_parameter.
    def enterC_external_parameter(self, ctx:PlSqlParser.C_external_parameterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_external_parameter.
    def exitC_external_parameter(self, ctx:PlSqlParser.C_external_parameterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#c_property.
    def enterC_property(self, ctx:PlSqlParser.C_propertyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#c_property.
    def exitC_property(self, ctx:PlSqlParser.C_propertyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter.
    def enterParameter(self, ctx:PlSqlParser.ParameterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter.
    def exitParameter(self, ctx:PlSqlParser.ParameterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#default_value_part.
    def enterDefault_value_part(self, ctx:PlSqlParser.Default_value_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#default_value_part.
    def exitDefault_value_part(self, ctx:PlSqlParser.Default_value_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#seq_of_declare_specs.
    def enterSeq_of_declare_specs(self, ctx:PlSqlParser.Seq_of_declare_specsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#seq_of_declare_specs.
    def exitSeq_of_declare_specs(self, ctx:PlSqlParser.Seq_of_declare_specsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#declare_spec.
    def enterDeclare_spec(self, ctx:PlSqlParser.Declare_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#declare_spec.
    def exitDeclare_spec(self, ctx:PlSqlParser.Declare_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#variable_declaration.
    def enterVariable_declaration(self, ctx:PlSqlParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#variable_declaration.
    def exitVariable_declaration(self, ctx:PlSqlParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subtype_declaration.
    def enterSubtype_declaration(self, ctx:PlSqlParser.Subtype_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subtype_declaration.
    def exitSubtype_declaration(self, ctx:PlSqlParser.Subtype_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_declaration.
    def enterCursor_declaration(self, ctx:PlSqlParser.Cursor_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_declaration.
    def exitCursor_declaration(self, ctx:PlSqlParser.Cursor_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter_spec.
    def enterParameter_spec(self, ctx:PlSqlParser.Parameter_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter_spec.
    def exitParameter_spec(self, ctx:PlSqlParser.Parameter_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_declaration.
    def enterException_declaration(self, ctx:PlSqlParser.Exception_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_declaration.
    def exitException_declaration(self, ctx:PlSqlParser.Exception_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pragma_declaration.
    def enterPragma_declaration(self, ctx:PlSqlParser.Pragma_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pragma_declaration.
    def exitPragma_declaration(self, ctx:PlSqlParser.Pragma_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_type_def.
    def enterRecord_type_def(self, ctx:PlSqlParser.Record_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_type_def.
    def exitRecord_type_def(self, ctx:PlSqlParser.Record_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#field_spec.
    def enterField_spec(self, ctx:PlSqlParser.Field_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#field_spec.
    def exitField_spec(self, ctx:PlSqlParser.Field_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#ref_cursor_type_def.
    def enterRef_cursor_type_def(self, ctx:PlSqlParser.Ref_cursor_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#ref_cursor_type_def.
    def exitRef_cursor_type_def(self, ctx:PlSqlParser.Ref_cursor_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_declaration.
    def enterType_declaration(self, ctx:PlSqlParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_declaration.
    def exitType_declaration(self, ctx:PlSqlParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_type_def.
    def enterTable_type_def(self, ctx:PlSqlParser.Table_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_type_def.
    def exitTable_type_def(self, ctx:PlSqlParser.Table_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_indexed_by_part.
    def enterTable_indexed_by_part(self, ctx:PlSqlParser.Table_indexed_by_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_indexed_by_part.
    def exitTable_indexed_by_part(self, ctx:PlSqlParser.Table_indexed_by_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#varray_type_def.
    def enterVarray_type_def(self, ctx:PlSqlParser.Varray_type_defContext):
        pass

    # Exit a parse tree produced by PlSqlParser#varray_type_def.
    def exitVarray_type_def(self, ctx:PlSqlParser.Varray_type_defContext):
        pass


    # Enter a parse tree produced by PlSqlParser#seq_of_statements.
    def enterSeq_of_statements(self, ctx:PlSqlParser.Seq_of_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#seq_of_statements.
    def exitSeq_of_statements(self, ctx:PlSqlParser.Seq_of_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#label_declaration.
    def enterLabel_declaration(self, ctx:PlSqlParser.Label_declarationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#label_declaration.
    def exitLabel_declaration(self, ctx:PlSqlParser.Label_declarationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#statement.
    def enterStatement(self, ctx:PlSqlParser.StatementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#statement.
    def exitStatement(self, ctx:PlSqlParser.StatementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#swallow_to_semi.
    def enterSwallow_to_semi(self, ctx:PlSqlParser.Swallow_to_semiContext):
        pass

    # Exit a parse tree produced by PlSqlParser#swallow_to_semi.
    def exitSwallow_to_semi(self, ctx:PlSqlParser.Swallow_to_semiContext):
        pass


    # Enter a parse tree produced by PlSqlParser#assignment_statement.
    def enterAssignment_statement(self, ctx:PlSqlParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#assignment_statement.
    def exitAssignment_statement(self, ctx:PlSqlParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#continue_statement.
    def enterContinue_statement(self, ctx:PlSqlParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#continue_statement.
    def exitContinue_statement(self, ctx:PlSqlParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exit_statement.
    def enterExit_statement(self, ctx:PlSqlParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exit_statement.
    def exitExit_statement(self, ctx:PlSqlParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#goto_statement.
    def enterGoto_statement(self, ctx:PlSqlParser.Goto_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#goto_statement.
    def exitGoto_statement(self, ctx:PlSqlParser.Goto_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#if_statement.
    def enterIf_statement(self, ctx:PlSqlParser.If_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#if_statement.
    def exitIf_statement(self, ctx:PlSqlParser.If_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#elsif_part.
    def enterElsif_part(self, ctx:PlSqlParser.Elsif_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#elsif_part.
    def exitElsif_part(self, ctx:PlSqlParser.Elsif_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#else_part.
    def enterElse_part(self, ctx:PlSqlParser.Else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#else_part.
    def exitElse_part(self, ctx:PlSqlParser.Else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#loop_statement.
    def enterLoop_statement(self, ctx:PlSqlParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#loop_statement.
    def exitLoop_statement(self, ctx:PlSqlParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_loop_param.
    def enterCursor_loop_param(self, ctx:PlSqlParser.Cursor_loop_paramContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_loop_param.
    def exitCursor_loop_param(self, ctx:PlSqlParser.Cursor_loop_paramContext):
        pass


    # Enter a parse tree produced by PlSqlParser#forall_statement.
    def enterForall_statement(self, ctx:PlSqlParser.Forall_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#forall_statement.
    def exitForall_statement(self, ctx:PlSqlParser.Forall_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#bounds_clause.
    def enterBounds_clause(self, ctx:PlSqlParser.Bounds_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#bounds_clause.
    def exitBounds_clause(self, ctx:PlSqlParser.Bounds_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#between_bound.
    def enterBetween_bound(self, ctx:PlSqlParser.Between_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#between_bound.
    def exitBetween_bound(self, ctx:PlSqlParser.Between_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lower_bound.
    def enterLower_bound(self, ctx:PlSqlParser.Lower_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lower_bound.
    def exitLower_bound(self, ctx:PlSqlParser.Lower_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#upper_bound.
    def enterUpper_bound(self, ctx:PlSqlParser.Upper_boundContext):
        pass

    # Exit a parse tree produced by PlSqlParser#upper_bound.
    def exitUpper_bound(self, ctx:PlSqlParser.Upper_boundContext):
        pass


    # Enter a parse tree produced by PlSqlParser#null_statement.
    def enterNull_statement(self, ctx:PlSqlParser.Null_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#null_statement.
    def exitNull_statement(self, ctx:PlSqlParser.Null_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#raise_statement.
    def enterRaise_statement(self, ctx:PlSqlParser.Raise_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#raise_statement.
    def exitRaise_statement(self, ctx:PlSqlParser.Raise_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#return_statement.
    def enterReturn_statement(self, ctx:PlSqlParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#return_statement.
    def exitReturn_statement(self, ctx:PlSqlParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#call_statement.
    def enterCall_statement(self, ctx:PlSqlParser.Call_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#call_statement.
    def exitCall_statement(self, ctx:PlSqlParser.Call_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pipe_row_statement.
    def enterPipe_row_statement(self, ctx:PlSqlParser.Pipe_row_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pipe_row_statement.
    def exitPipe_row_statement(self, ctx:PlSqlParser.Pipe_row_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#selection_directive.
    def enterSelection_directive(self, ctx:PlSqlParser.Selection_directiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#selection_directive.
    def exitSelection_directive(self, ctx:PlSqlParser.Selection_directiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_directive.
    def enterError_directive(self, ctx:PlSqlParser.Error_directiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_directive.
    def exitError_directive(self, ctx:PlSqlParser.Error_directiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#selection_directive_body.
    def enterSelection_directive_body(self, ctx:PlSqlParser.Selection_directive_bodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#selection_directive_body.
    def exitSelection_directive_body(self, ctx:PlSqlParser.Selection_directive_bodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#body.
    def enterBody(self, ctx:PlSqlParser.BodyContext):
        pass

    # Exit a parse tree produced by PlSqlParser#body.
    def exitBody(self, ctx:PlSqlParser.BodyContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_handler.
    def enterException_handler(self, ctx:PlSqlParser.Exception_handlerContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_handler.
    def exitException_handler(self, ctx:PlSqlParser.Exception_handlerContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_block.
    def enterTrigger_block(self, ctx:PlSqlParser.Trigger_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_block.
    def exitTrigger_block(self, ctx:PlSqlParser.Trigger_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tps_block.
    def enterTps_block(self, ctx:PlSqlParser.Tps_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tps_block.
    def exitTps_block(self, ctx:PlSqlParser.Tps_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#block.
    def enterBlock(self, ctx:PlSqlParser.BlockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#block.
    def exitBlock(self, ctx:PlSqlParser.BlockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_statement.
    def enterSql_statement(self, ctx:PlSqlParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_statement.
    def exitSql_statement(self, ctx:PlSqlParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#execute_immediate.
    def enterExecute_immediate(self, ctx:PlSqlParser.Execute_immediateContext):
        pass

    # Exit a parse tree produced by PlSqlParser#execute_immediate.
    def exitExecute_immediate(self, ctx:PlSqlParser.Execute_immediateContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dynamic_returning_clause.
    def enterDynamic_returning_clause(self, ctx:PlSqlParser.Dynamic_returning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dynamic_returning_clause.
    def exitDynamic_returning_clause(self, ctx:PlSqlParser.Dynamic_returning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#data_manipulation_language_statements.
    def enterData_manipulation_language_statements(self, ctx:PlSqlParser.Data_manipulation_language_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#data_manipulation_language_statements.
    def exitData_manipulation_language_statements(self, ctx:PlSqlParser.Data_manipulation_language_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_manipulation_statements.
    def enterCursor_manipulation_statements(self, ctx:PlSqlParser.Cursor_manipulation_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_manipulation_statements.
    def exitCursor_manipulation_statements(self, ctx:PlSqlParser.Cursor_manipulation_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#close_statement.
    def enterClose_statement(self, ctx:PlSqlParser.Close_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#close_statement.
    def exitClose_statement(self, ctx:PlSqlParser.Close_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#open_statement.
    def enterOpen_statement(self, ctx:PlSqlParser.Open_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#open_statement.
    def exitOpen_statement(self, ctx:PlSqlParser.Open_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#fetch_statement.
    def enterFetch_statement(self, ctx:PlSqlParser.Fetch_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#fetch_statement.
    def exitFetch_statement(self, ctx:PlSqlParser.Fetch_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#variable_or_collection.
    def enterVariable_or_collection(self, ctx:PlSqlParser.Variable_or_collectionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#variable_or_collection.
    def exitVariable_or_collection(self, ctx:PlSqlParser.Variable_or_collectionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#open_for_statement.
    def enterOpen_for_statement(self, ctx:PlSqlParser.Open_for_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#open_for_statement.
    def exitOpen_for_statement(self, ctx:PlSqlParser.Open_for_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#transaction_control_statements.
    def enterTransaction_control_statements(self, ctx:PlSqlParser.Transaction_control_statementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#transaction_control_statements.
    def exitTransaction_control_statements(self, ctx:PlSqlParser.Transaction_control_statementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_transaction_command.
    def enterSet_transaction_command(self, ctx:PlSqlParser.Set_transaction_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_transaction_command.
    def exitSet_transaction_command(self, ctx:PlSqlParser.Set_transaction_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_constraint_command.
    def enterSet_constraint_command(self, ctx:PlSqlParser.Set_constraint_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_constraint_command.
    def exitSet_constraint_command(self, ctx:PlSqlParser.Set_constraint_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#commit_statement.
    def enterCommit_statement(self, ctx:PlSqlParser.Commit_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#commit_statement.
    def exitCommit_statement(self, ctx:PlSqlParser.Commit_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#write_clause.
    def enterWrite_clause(self, ctx:PlSqlParser.Write_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#write_clause.
    def exitWrite_clause(self, ctx:PlSqlParser.Write_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollback_statement.
    def enterRollback_statement(self, ctx:PlSqlParser.Rollback_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollback_statement.
    def exitRollback_statement(self, ctx:PlSqlParser.Rollback_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#savepoint_statement.
    def enterSavepoint_statement(self, ctx:PlSqlParser.Savepoint_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#savepoint_statement.
    def exitSavepoint_statement(self, ctx:PlSqlParser.Savepoint_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collection_method_call.
    def enterCollection_method_call(self, ctx:PlSqlParser.Collection_method_callContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collection_method_call.
    def exitCollection_method_call(self, ctx:PlSqlParser.Collection_method_callContext):
        pass


    # Enter a parse tree produced by PlSqlParser#explain_statement.
    def enterExplain_statement(self, ctx:PlSqlParser.Explain_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#explain_statement.
    def exitExplain_statement(self, ctx:PlSqlParser.Explain_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#select_only_statement.
    def enterSelect_only_statement(self, ctx:PlSqlParser.Select_only_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#select_only_statement.
    def exitSelect_only_statement(self, ctx:PlSqlParser.Select_only_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#select_statement.
    def enterSelect_statement(self, ctx:PlSqlParser.Select_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#select_statement.
    def exitSelect_statement(self, ctx:PlSqlParser.Select_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#with_clause.
    def enterWith_clause(self, ctx:PlSqlParser.With_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#with_clause.
    def exitWith_clause(self, ctx:PlSqlParser.With_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#with_factoring_clause.
    def enterWith_factoring_clause(self, ctx:PlSqlParser.With_factoring_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#with_factoring_clause.
    def exitWith_factoring_clause(self, ctx:PlSqlParser.With_factoring_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_factoring_clause.
    def enterSubquery_factoring_clause(self, ctx:PlSqlParser.Subquery_factoring_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_factoring_clause.
    def exitSubquery_factoring_clause(self, ctx:PlSqlParser.Subquery_factoring_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#search_clause.
    def enterSearch_clause(self, ctx:PlSqlParser.Search_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#search_clause.
    def exitSearch_clause(self, ctx:PlSqlParser.Search_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cycle_clause.
    def enterCycle_clause(self, ctx:PlSqlParser.Cycle_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cycle_clause.
    def exitCycle_clause(self, ctx:PlSqlParser.Cycle_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subav_factoring_clause.
    def enterSubav_factoring_clause(self, ctx:PlSqlParser.Subav_factoring_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subav_factoring_clause.
    def exitSubav_factoring_clause(self, ctx:PlSqlParser.Subav_factoring_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subav_clause.
    def enterSubav_clause(self, ctx:PlSqlParser.Subav_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subav_clause.
    def exitSubav_clause(self, ctx:PlSqlParser.Subav_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hierarchies_clause.
    def enterHierarchies_clause(self, ctx:PlSqlParser.Hierarchies_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hierarchies_clause.
    def exitHierarchies_clause(self, ctx:PlSqlParser.Hierarchies_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filter_clauses.
    def enterFilter_clauses(self, ctx:PlSqlParser.Filter_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filter_clauses.
    def exitFilter_clauses(self, ctx:PlSqlParser.Filter_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#filter_clause.
    def enterFilter_clause(self, ctx:PlSqlParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#filter_clause.
    def exitFilter_clause(self, ctx:PlSqlParser.Filter_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_calcs_clause.
    def enterAdd_calcs_clause(self, ctx:PlSqlParser.Add_calcs_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_calcs_clause.
    def exitAdd_calcs_clause(self, ctx:PlSqlParser.Add_calcs_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#add_calc_meas_clause.
    def enterAdd_calc_meas_clause(self, ctx:PlSqlParser.Add_calc_meas_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#add_calc_meas_clause.
    def exitAdd_calc_meas_clause(self, ctx:PlSqlParser.Add_calc_meas_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery.
    def enterSubquery(self, ctx:PlSqlParser.SubqueryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery.
    def exitSubquery(self, ctx:PlSqlParser.SubqueryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_basic_elements.
    def enterSubquery_basic_elements(self, ctx:PlSqlParser.Subquery_basic_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_basic_elements.
    def exitSubquery_basic_elements(self, ctx:PlSqlParser.Subquery_basic_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_operation_part.
    def enterSubquery_operation_part(self, ctx:PlSqlParser.Subquery_operation_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_operation_part.
    def exitSubquery_operation_part(self, ctx:PlSqlParser.Subquery_operation_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_block.
    def enterQuery_block(self, ctx:PlSqlParser.Query_blockContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_block.
    def exitQuery_block(self, ctx:PlSqlParser.Query_blockContext):
        pass


    # Enter a parse tree produced by PlSqlParser#selected_list.
    def enterSelected_list(self, ctx:PlSqlParser.Selected_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#selected_list.
    def exitSelected_list(self, ctx:PlSqlParser.Selected_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#from_clause.
    def enterFrom_clause(self, ctx:PlSqlParser.From_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#from_clause.
    def exitFrom_clause(self, ctx:PlSqlParser.From_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#select_list_elements.
    def enterSelect_list_elements(self, ctx:PlSqlParser.Select_list_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#select_list_elements.
    def exitSelect_list_elements(self, ctx:PlSqlParser.Select_list_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_list.
    def enterTable_ref_list(self, ctx:PlSqlParser.Table_ref_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_list.
    def exitTable_ref_list(self, ctx:PlSqlParser.Table_ref_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref.
    def enterTable_ref(self, ctx:PlSqlParser.Table_refContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref.
    def exitTable_ref(self, ctx:PlSqlParser.Table_refContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_aux.
    def enterTable_ref_aux(self, ctx:PlSqlParser.Table_ref_auxContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_aux.
    def exitTable_ref_aux(self, ctx:PlSqlParser.Table_ref_auxContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_aux_internal_one.
    def enterTable_ref_aux_internal_one(self, ctx:PlSqlParser.Table_ref_aux_internal_oneContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_aux_internal_one.
    def exitTable_ref_aux_internal_one(self, ctx:PlSqlParser.Table_ref_aux_internal_oneContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_aux_internal_two.
    def enterTable_ref_aux_internal_two(self, ctx:PlSqlParser.Table_ref_aux_internal_twoContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_aux_internal_two.
    def exitTable_ref_aux_internal_two(self, ctx:PlSqlParser.Table_ref_aux_internal_twoContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_ref_aux_internal_thre.
    def enterTable_ref_aux_internal_thre(self, ctx:PlSqlParser.Table_ref_aux_internal_threContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_ref_aux_internal_thre.
    def exitTable_ref_aux_internal_thre(self, ctx:PlSqlParser.Table_ref_aux_internal_threContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_clause.
    def enterJoin_clause(self, ctx:PlSqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_clause.
    def exitJoin_clause(self, ctx:PlSqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_on_part.
    def enterJoin_on_part(self, ctx:PlSqlParser.Join_on_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_on_part.
    def exitJoin_on_part(self, ctx:PlSqlParser.Join_on_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#join_using_part.
    def enterJoin_using_part(self, ctx:PlSqlParser.Join_using_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#join_using_part.
    def exitJoin_using_part(self, ctx:PlSqlParser.Join_using_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#outer_join_type.
    def enterOuter_join_type(self, ctx:PlSqlParser.Outer_join_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#outer_join_type.
    def exitOuter_join_type(self, ctx:PlSqlParser.Outer_join_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_partition_clause.
    def enterQuery_partition_clause(self, ctx:PlSqlParser.Query_partition_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_partition_clause.
    def exitQuery_partition_clause(self, ctx:PlSqlParser.Query_partition_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#flashback_query_clause.
    def enterFlashback_query_clause(self, ctx:PlSqlParser.Flashback_query_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#flashback_query_clause.
    def exitFlashback_query_clause(self, ctx:PlSqlParser.Flashback_query_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_clause.
    def enterPivot_clause(self, ctx:PlSqlParser.Pivot_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_clause.
    def exitPivot_clause(self, ctx:PlSqlParser.Pivot_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_element.
    def enterPivot_element(self, ctx:PlSqlParser.Pivot_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_element.
    def exitPivot_element(self, ctx:PlSqlParser.Pivot_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_for_clause.
    def enterPivot_for_clause(self, ctx:PlSqlParser.Pivot_for_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_for_clause.
    def exitPivot_for_clause(self, ctx:PlSqlParser.Pivot_for_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause.
    def enterPivot_in_clause(self, ctx:PlSqlParser.Pivot_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause.
    def exitPivot_in_clause(self, ctx:PlSqlParser.Pivot_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause_element.
    def enterPivot_in_clause_element(self, ctx:PlSqlParser.Pivot_in_clause_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause_element.
    def exitPivot_in_clause_element(self, ctx:PlSqlParser.Pivot_in_clause_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#pivot_in_clause_elements.
    def enterPivot_in_clause_elements(self, ctx:PlSqlParser.Pivot_in_clause_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#pivot_in_clause_elements.
    def exitPivot_in_clause_elements(self, ctx:PlSqlParser.Pivot_in_clause_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_clause.
    def enterUnpivot_clause(self, ctx:PlSqlParser.Unpivot_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_clause.
    def exitUnpivot_clause(self, ctx:PlSqlParser.Unpivot_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_in_clause.
    def enterUnpivot_in_clause(self, ctx:PlSqlParser.Unpivot_in_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_in_clause.
    def exitUnpivot_in_clause(self, ctx:PlSqlParser.Unpivot_in_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unpivot_in_elements.
    def enterUnpivot_in_elements(self, ctx:PlSqlParser.Unpivot_in_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unpivot_in_elements.
    def exitUnpivot_in_elements(self, ctx:PlSqlParser.Unpivot_in_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#hierarchical_query_clause.
    def enterHierarchical_query_clause(self, ctx:PlSqlParser.Hierarchical_query_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#hierarchical_query_clause.
    def exitHierarchical_query_clause(self, ctx:PlSqlParser.Hierarchical_query_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#start_part.
    def enterStart_part(self, ctx:PlSqlParser.Start_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#start_part.
    def exitStart_part(self, ctx:PlSqlParser.Start_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:PlSqlParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:PlSqlParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#group_by_elements.
    def enterGroup_by_elements(self, ctx:PlSqlParser.Group_by_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#group_by_elements.
    def exitGroup_by_elements(self, ctx:PlSqlParser.Group_by_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollup_cube_clause.
    def enterRollup_cube_clause(self, ctx:PlSqlParser.Rollup_cube_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollup_cube_clause.
    def exitRollup_cube_clause(self, ctx:PlSqlParser.Rollup_cube_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:PlSqlParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:PlSqlParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grouping_sets_elements.
    def enterGrouping_sets_elements(self, ctx:PlSqlParser.Grouping_sets_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grouping_sets_elements.
    def exitGrouping_sets_elements(self, ctx:PlSqlParser.Grouping_sets_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#having_clause.
    def enterHaving_clause(self, ctx:PlSqlParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#having_clause.
    def exitHaving_clause(self, ctx:PlSqlParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_clause.
    def enterModel_clause(self, ctx:PlSqlParser.Model_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_clause.
    def exitModel_clause(self, ctx:PlSqlParser.Model_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cell_reference_options.
    def enterCell_reference_options(self, ctx:PlSqlParser.Cell_reference_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cell_reference_options.
    def exitCell_reference_options(self, ctx:PlSqlParser.Cell_reference_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#return_rows_clause.
    def enterReturn_rows_clause(self, ctx:PlSqlParser.Return_rows_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#return_rows_clause.
    def exitReturn_rows_clause(self, ctx:PlSqlParser.Return_rows_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_model.
    def enterReference_model(self, ctx:PlSqlParser.Reference_modelContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_model.
    def exitReference_model(self, ctx:PlSqlParser.Reference_modelContext):
        pass


    # Enter a parse tree produced by PlSqlParser#main_model.
    def enterMain_model(self, ctx:PlSqlParser.Main_modelContext):
        pass

    # Exit a parse tree produced by PlSqlParser#main_model.
    def exitMain_model(self, ctx:PlSqlParser.Main_modelContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_clauses.
    def enterModel_column_clauses(self, ctx:PlSqlParser.Model_column_clausesContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_clauses.
    def exitModel_column_clauses(self, ctx:PlSqlParser.Model_column_clausesContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_partition_part.
    def enterModel_column_partition_part(self, ctx:PlSqlParser.Model_column_partition_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_partition_part.
    def exitModel_column_partition_part(self, ctx:PlSqlParser.Model_column_partition_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column_list.
    def enterModel_column_list(self, ctx:PlSqlParser.Model_column_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column_list.
    def exitModel_column_list(self, ctx:PlSqlParser.Model_column_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_column.
    def enterModel_column(self, ctx:PlSqlParser.Model_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_column.
    def exitModel_column(self, ctx:PlSqlParser.Model_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_clause.
    def enterModel_rules_clause(self, ctx:PlSqlParser.Model_rules_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_clause.
    def exitModel_rules_clause(self, ctx:PlSqlParser.Model_rules_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_part.
    def enterModel_rules_part(self, ctx:PlSqlParser.Model_rules_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_part.
    def exitModel_rules_part(self, ctx:PlSqlParser.Model_rules_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_rules_element.
    def enterModel_rules_element(self, ctx:PlSqlParser.Model_rules_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_rules_element.
    def exitModel_rules_element(self, ctx:PlSqlParser.Model_rules_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cell_assignment.
    def enterCell_assignment(self, ctx:PlSqlParser.Cell_assignmentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cell_assignment.
    def exitCell_assignment(self, ctx:PlSqlParser.Cell_assignmentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_iterate_clause.
    def enterModel_iterate_clause(self, ctx:PlSqlParser.Model_iterate_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_iterate_clause.
    def exitModel_iterate_clause(self, ctx:PlSqlParser.Model_iterate_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#until_part.
    def enterUntil_part(self, ctx:PlSqlParser.Until_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#until_part.
    def exitUntil_part(self, ctx:PlSqlParser.Until_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:PlSqlParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:PlSqlParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#order_by_elements.
    def enterOrder_by_elements(self, ctx:PlSqlParser.Order_by_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#order_by_elements.
    def exitOrder_by_elements(self, ctx:PlSqlParser.Order_by_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#offset_clause.
    def enterOffset_clause(self, ctx:PlSqlParser.Offset_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#offset_clause.
    def exitOffset_clause(self, ctx:PlSqlParser.Offset_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#fetch_clause.
    def enterFetch_clause(self, ctx:PlSqlParser.Fetch_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#fetch_clause.
    def exitFetch_clause(self, ctx:PlSqlParser.Fetch_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_clause.
    def enterFor_update_clause(self, ctx:PlSqlParser.For_update_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_clause.
    def exitFor_update_clause(self, ctx:PlSqlParser.For_update_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_of_part.
    def enterFor_update_of_part(self, ctx:PlSqlParser.For_update_of_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_of_part.
    def exitFor_update_of_part(self, ctx:PlSqlParser.For_update_of_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#for_update_options.
    def enterFor_update_options(self, ctx:PlSqlParser.For_update_optionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#for_update_options.
    def exitFor_update_options(self, ctx:PlSqlParser.For_update_optionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_statement.
    def enterUpdate_statement(self, ctx:PlSqlParser.Update_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_statement.
    def exitUpdate_statement(self, ctx:PlSqlParser.Update_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#update_set_clause.
    def enterUpdate_set_clause(self, ctx:PlSqlParser.Update_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#update_set_clause.
    def exitUpdate_set_clause(self, ctx:PlSqlParser.Update_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_based_update_set_clause.
    def enterColumn_based_update_set_clause(self, ctx:PlSqlParser.Column_based_update_set_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_based_update_set_clause.
    def exitColumn_based_update_set_clause(self, ctx:PlSqlParser.Column_based_update_set_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#delete_statement.
    def enterDelete_statement(self, ctx:PlSqlParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#delete_statement.
    def exitDelete_statement(self, ctx:PlSqlParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#insert_statement.
    def enterInsert_statement(self, ctx:PlSqlParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#insert_statement.
    def exitInsert_statement(self, ctx:PlSqlParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#single_table_insert.
    def enterSingle_table_insert(self, ctx:PlSqlParser.Single_table_insertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#single_table_insert.
    def exitSingle_table_insert(self, ctx:PlSqlParser.Single_table_insertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_table_insert.
    def enterMulti_table_insert(self, ctx:PlSqlParser.Multi_table_insertContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_table_insert.
    def exitMulti_table_insert(self, ctx:PlSqlParser.Multi_table_insertContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_table_element.
    def enterMulti_table_element(self, ctx:PlSqlParser.Multi_table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_table_element.
    def exitMulti_table_element(self, ctx:PlSqlParser.Multi_table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_clause.
    def enterConditional_insert_clause(self, ctx:PlSqlParser.Conditional_insert_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_clause.
    def exitConditional_insert_clause(self, ctx:PlSqlParser.Conditional_insert_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_when_part.
    def enterConditional_insert_when_part(self, ctx:PlSqlParser.Conditional_insert_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_when_part.
    def exitConditional_insert_when_part(self, ctx:PlSqlParser.Conditional_insert_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#conditional_insert_else_part.
    def enterConditional_insert_else_part(self, ctx:PlSqlParser.Conditional_insert_else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#conditional_insert_else_part.
    def exitConditional_insert_else_part(self, ctx:PlSqlParser.Conditional_insert_else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#insert_into_clause.
    def enterInsert_into_clause(self, ctx:PlSqlParser.Insert_into_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#insert_into_clause.
    def exitInsert_into_clause(self, ctx:PlSqlParser.Insert_into_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#values_clause.
    def enterValues_clause(self, ctx:PlSqlParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#values_clause.
    def exitValues_clause(self, ctx:PlSqlParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_statement.
    def enterMerge_statement(self, ctx:PlSqlParser.Merge_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_statement.
    def exitMerge_statement(self, ctx:PlSqlParser.Merge_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:PlSqlParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:PlSqlParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_element.
    def enterMerge_element(self, ctx:PlSqlParser.Merge_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_element.
    def exitMerge_element(self, ctx:PlSqlParser.Merge_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_update_delete_part.
    def enterMerge_update_delete_part(self, ctx:PlSqlParser.Merge_update_delete_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_update_delete_part.
    def exitMerge_update_delete_part(self, ctx:PlSqlParser.Merge_update_delete_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:PlSqlParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:PlSqlParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#selected_tableview.
    def enterSelected_tableview(self, ctx:PlSqlParser.Selected_tableviewContext):
        pass

    # Exit a parse tree produced by PlSqlParser#selected_tableview.
    def exitSelected_tableview(self, ctx:PlSqlParser.Selected_tableviewContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_table_statement.
    def enterLock_table_statement(self, ctx:PlSqlParser.Lock_table_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_table_statement.
    def exitLock_table_statement(self, ctx:PlSqlParser.Lock_table_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#wait_nowait_part.
    def enterWait_nowait_part(self, ctx:PlSqlParser.Wait_nowait_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#wait_nowait_part.
    def exitWait_nowait_part(self, ctx:PlSqlParser.Wait_nowait_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_table_element.
    def enterLock_table_element(self, ctx:PlSqlParser.Lock_table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_table_element.
    def exitLock_table_element(self, ctx:PlSqlParser.Lock_table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#lock_mode.
    def enterLock_mode(self, ctx:PlSqlParser.Lock_modeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#lock_mode.
    def exitLock_mode(self, ctx:PlSqlParser.Lock_modeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#general_table_ref.
    def enterGeneral_table_ref(self, ctx:PlSqlParser.General_table_refContext):
        pass

    # Exit a parse tree produced by PlSqlParser#general_table_ref.
    def exitGeneral_table_ref(self, ctx:PlSqlParser.General_table_refContext):
        pass


    # Enter a parse tree produced by PlSqlParser#static_returning_clause.
    def enterStatic_returning_clause(self, ctx:PlSqlParser.Static_returning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#static_returning_clause.
    def exitStatic_returning_clause(self, ctx:PlSqlParser.Static_returning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_clause.
    def enterError_logging_clause(self, ctx:PlSqlParser.Error_logging_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_clause.
    def exitError_logging_clause(self, ctx:PlSqlParser.Error_logging_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_into_part.
    def enterError_logging_into_part(self, ctx:PlSqlParser.Error_logging_into_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_into_part.
    def exitError_logging_into_part(self, ctx:PlSqlParser.Error_logging_into_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#error_logging_reject_part.
    def enterError_logging_reject_part(self, ctx:PlSqlParser.Error_logging_reject_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#error_logging_reject_part.
    def exitError_logging_reject_part(self, ctx:PlSqlParser.Error_logging_reject_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dml_table_expression_clause.
    def enterDml_table_expression_clause(self, ctx:PlSqlParser.Dml_table_expression_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dml_table_expression_clause.
    def exitDml_table_expression_clause(self, ctx:PlSqlParser.Dml_table_expression_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_collection_expression.
    def enterTable_collection_expression(self, ctx:PlSqlParser.Table_collection_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_collection_expression.
    def exitTable_collection_expression(self, ctx:PlSqlParser.Table_collection_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#subquery_restriction_clause.
    def enterSubquery_restriction_clause(self, ctx:PlSqlParser.Subquery_restriction_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#subquery_restriction_clause.
    def exitSubquery_restriction_clause(self, ctx:PlSqlParser.Subquery_restriction_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sample_clause.
    def enterSample_clause(self, ctx:PlSqlParser.Sample_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sample_clause.
    def exitSample_clause(self, ctx:PlSqlParser.Sample_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#seed_part.
    def enterSeed_part(self, ctx:PlSqlParser.Seed_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#seed_part.
    def exitSeed_part(self, ctx:PlSqlParser.Seed_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#condition.
    def enterCondition(self, ctx:PlSqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#condition.
    def exitCondition(self, ctx:PlSqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#expressions.
    def enterExpressions(self, ctx:PlSqlParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#expressions.
    def exitExpressions(self, ctx:PlSqlParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#expression.
    def enterExpression(self, ctx:PlSqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#expression.
    def exitExpression(self, ctx:PlSqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_expression.
    def enterCursor_expression(self, ctx:PlSqlParser.Cursor_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_expression.
    def exitCursor_expression(self, ctx:PlSqlParser.Cursor_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logical_expression.
    def enterLogical_expression(self, ctx:PlSqlParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logical_expression.
    def exitLogical_expression(self, ctx:PlSqlParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unary_logical_expression.
    def enterUnary_logical_expression(self, ctx:PlSqlParser.Unary_logical_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unary_logical_expression.
    def exitUnary_logical_expression(self, ctx:PlSqlParser.Unary_logical_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unary_logical_operation.
    def enterUnary_logical_operation(self, ctx:PlSqlParser.Unary_logical_operationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unary_logical_operation.
    def exitUnary_logical_operation(self, ctx:PlSqlParser.Unary_logical_operationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#logical_operation.
    def enterLogical_operation(self, ctx:PlSqlParser.Logical_operationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#logical_operation.
    def exitLogical_operation(self, ctx:PlSqlParser.Logical_operationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multiset_expression.
    def enterMultiset_expression(self, ctx:PlSqlParser.Multiset_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multiset_expression.
    def exitMultiset_expression(self, ctx:PlSqlParser.Multiset_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relational_expression.
    def enterRelational_expression(self, ctx:PlSqlParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relational_expression.
    def exitRelational_expression(self, ctx:PlSqlParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#compound_expression.
    def enterCompound_expression(self, ctx:PlSqlParser.Compound_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#compound_expression.
    def exitCompound_expression(self, ctx:PlSqlParser.Compound_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#relational_operator.
    def enterRelational_operator(self, ctx:PlSqlParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by PlSqlParser#relational_operator.
    def exitRelational_operator(self, ctx:PlSqlParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by PlSqlParser#in_elements.
    def enterIn_elements(self, ctx:PlSqlParser.In_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#in_elements.
    def exitIn_elements(self, ctx:PlSqlParser.In_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#between_elements.
    def enterBetween_elements(self, ctx:PlSqlParser.Between_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#between_elements.
    def exitBetween_elements(self, ctx:PlSqlParser.Between_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#concatenation.
    def enterConcatenation(self, ctx:PlSqlParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by PlSqlParser#concatenation.
    def exitConcatenation(self, ctx:PlSqlParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by PlSqlParser#interval_expression.
    def enterInterval_expression(self, ctx:PlSqlParser.Interval_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#interval_expression.
    def exitInterval_expression(self, ctx:PlSqlParser.Interval_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_expression.
    def enterModel_expression(self, ctx:PlSqlParser.Model_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_expression.
    def exitModel_expression(self, ctx:PlSqlParser.Model_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#model_expression_element.
    def enterModel_expression_element(self, ctx:PlSqlParser.Model_expression_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#model_expression_element.
    def exitModel_expression_element(self, ctx:PlSqlParser.Model_expression_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#single_column_for_loop.
    def enterSingle_column_for_loop(self, ctx:PlSqlParser.Single_column_for_loopContext):
        pass

    # Exit a parse tree produced by PlSqlParser#single_column_for_loop.
    def exitSingle_column_for_loop(self, ctx:PlSqlParser.Single_column_for_loopContext):
        pass


    # Enter a parse tree produced by PlSqlParser#multi_column_for_loop.
    def enterMulti_column_for_loop(self, ctx:PlSqlParser.Multi_column_for_loopContext):
        pass

    # Exit a parse tree produced by PlSqlParser#multi_column_for_loop.
    def exitMulti_column_for_loop(self, ctx:PlSqlParser.Multi_column_for_loopContext):
        pass


    # Enter a parse tree produced by PlSqlParser#unary_expression.
    def enterUnary_expression(self, ctx:PlSqlParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#unary_expression.
    def exitUnary_expression(self, ctx:PlSqlParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#implicit_cursor_expression.
    def enterImplicit_cursor_expression(self, ctx:PlSqlParser.Implicit_cursor_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#implicit_cursor_expression.
    def exitImplicit_cursor_expression(self, ctx:PlSqlParser.Implicit_cursor_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collection_expression.
    def enterCollection_expression(self, ctx:PlSqlParser.Collection_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collection_expression.
    def exitCollection_expression(self, ctx:PlSqlParser.Collection_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#case_statement.
    def enterCase_statement(self, ctx:PlSqlParser.Case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#case_statement.
    def exitCase_statement(self, ctx:PlSqlParser.Case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_case_statement.
    def enterSimple_case_statement(self, ctx:PlSqlParser.Simple_case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_case_statement.
    def exitSimple_case_statement(self, ctx:PlSqlParser.Simple_case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#simple_case_when_part.
    def enterSimple_case_when_part(self, ctx:PlSqlParser.Simple_case_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#simple_case_when_part.
    def exitSimple_case_when_part(self, ctx:PlSqlParser.Simple_case_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#searched_case_statement.
    def enterSearched_case_statement(self, ctx:PlSqlParser.Searched_case_statementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#searched_case_statement.
    def exitSearched_case_statement(self, ctx:PlSqlParser.Searched_case_statementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#searched_case_when_part.
    def enterSearched_case_when_part(self, ctx:PlSqlParser.Searched_case_when_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#searched_case_when_part.
    def exitSearched_case_when_part(self, ctx:PlSqlParser.Searched_case_when_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#case_else_part.
    def enterCase_else_part(self, ctx:PlSqlParser.Case_else_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#case_else_part.
    def exitCase_else_part(self, ctx:PlSqlParser.Case_else_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#atom.
    def enterAtom(self, ctx:PlSqlParser.AtomContext):
        pass

    # Exit a parse tree produced by PlSqlParser#atom.
    def exitAtom(self, ctx:PlSqlParser.AtomContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quantified_expression.
    def enterQuantified_expression(self, ctx:PlSqlParser.Quantified_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quantified_expression.
    def exitQuantified_expression(self, ctx:PlSqlParser.Quantified_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#string_function.
    def enterString_function(self, ctx:PlSqlParser.String_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#string_function.
    def exitString_function(self, ctx:PlSqlParser.String_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#standard_function.
    def enterStandard_function(self, ctx:PlSqlParser.Standard_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#standard_function.
    def exitStandard_function(self, ctx:PlSqlParser.Standard_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_function.
    def enterJson_function(self, ctx:PlSqlParser.Json_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_function.
    def exitJson_function(self, ctx:PlSqlParser.Json_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_object_content.
    def enterJson_object_content(self, ctx:PlSqlParser.Json_object_contentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_object_content.
    def exitJson_object_content(self, ctx:PlSqlParser.Json_object_contentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_object_entry.
    def enterJson_object_entry(self, ctx:PlSqlParser.Json_object_entryContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_object_entry.
    def exitJson_object_entry(self, ctx:PlSqlParser.Json_object_entryContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_table_clause.
    def enterJson_table_clause(self, ctx:PlSqlParser.Json_table_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_table_clause.
    def exitJson_table_clause(self, ctx:PlSqlParser.Json_table_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_array_element.
    def enterJson_array_element(self, ctx:PlSqlParser.Json_array_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_array_element.
    def exitJson_array_element(self, ctx:PlSqlParser.Json_array_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_on_null_clause.
    def enterJson_on_null_clause(self, ctx:PlSqlParser.Json_on_null_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_on_null_clause.
    def exitJson_on_null_clause(self, ctx:PlSqlParser.Json_on_null_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_return_clause.
    def enterJson_return_clause(self, ctx:PlSqlParser.Json_return_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_return_clause.
    def exitJson_return_clause(self, ctx:PlSqlParser.Json_return_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_transform_op.
    def enterJson_transform_op(self, ctx:PlSqlParser.Json_transform_opContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_transform_op.
    def exitJson_transform_op(self, ctx:PlSqlParser.Json_transform_opContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_column_clause.
    def enterJson_column_clause(self, ctx:PlSqlParser.Json_column_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_column_clause.
    def exitJson_column_clause(self, ctx:PlSqlParser.Json_column_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_column_definition.
    def enterJson_column_definition(self, ctx:PlSqlParser.Json_column_definitionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_column_definition.
    def exitJson_column_definition(self, ctx:PlSqlParser.Json_column_definitionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_query_returning_clause.
    def enterJson_query_returning_clause(self, ctx:PlSqlParser.Json_query_returning_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_query_returning_clause.
    def exitJson_query_returning_clause(self, ctx:PlSqlParser.Json_query_returning_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_query_return_type.
    def enterJson_query_return_type(self, ctx:PlSqlParser.Json_query_return_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_query_return_type.
    def exitJson_query_return_type(self, ctx:PlSqlParser.Json_query_return_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_query_wrapper_clause.
    def enterJson_query_wrapper_clause(self, ctx:PlSqlParser.Json_query_wrapper_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_query_wrapper_clause.
    def exitJson_query_wrapper_clause(self, ctx:PlSqlParser.Json_query_wrapper_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_query_on_error_clause.
    def enterJson_query_on_error_clause(self, ctx:PlSqlParser.Json_query_on_error_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_query_on_error_clause.
    def exitJson_query_on_error_clause(self, ctx:PlSqlParser.Json_query_on_error_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_query_on_empty_clause.
    def enterJson_query_on_empty_clause(self, ctx:PlSqlParser.Json_query_on_empty_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_query_on_empty_clause.
    def exitJson_query_on_empty_clause(self, ctx:PlSqlParser.Json_query_on_empty_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_value_return_clause.
    def enterJson_value_return_clause(self, ctx:PlSqlParser.Json_value_return_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_value_return_clause.
    def exitJson_value_return_clause(self, ctx:PlSqlParser.Json_value_return_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_value_return_type.
    def enterJson_value_return_type(self, ctx:PlSqlParser.Json_value_return_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_value_return_type.
    def exitJson_value_return_type(self, ctx:PlSqlParser.Json_value_return_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#json_value_on_mismatch_clause.
    def enterJson_value_on_mismatch_clause(self, ctx:PlSqlParser.Json_value_on_mismatch_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#json_value_on_mismatch_clause.
    def exitJson_value_on_mismatch_clause(self, ctx:PlSqlParser.Json_value_on_mismatch_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#literal.
    def enterLiteral(self, ctx:PlSqlParser.LiteralContext):
        pass

    # Exit a parse tree produced by PlSqlParser#literal.
    def exitLiteral(self, ctx:PlSqlParser.LiteralContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric_function_wrapper.
    def enterNumeric_function_wrapper(self, ctx:PlSqlParser.Numeric_function_wrapperContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric_function_wrapper.
    def exitNumeric_function_wrapper(self, ctx:PlSqlParser.Numeric_function_wrapperContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric_function.
    def enterNumeric_function(self, ctx:PlSqlParser.Numeric_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric_function.
    def exitNumeric_function(self, ctx:PlSqlParser.Numeric_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#listagg_overflow_clause.
    def enterListagg_overflow_clause(self, ctx:PlSqlParser.Listagg_overflow_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#listagg_overflow_clause.
    def exitListagg_overflow_clause(self, ctx:PlSqlParser.Listagg_overflow_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#other_function.
    def enterOther_function(self, ctx:PlSqlParser.Other_functionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#other_function.
    def exitOther_function(self, ctx:PlSqlParser.Other_functionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#over_clause_keyword.
    def enterOver_clause_keyword(self, ctx:PlSqlParser.Over_clause_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#over_clause_keyword.
    def exitOver_clause_keyword(self, ctx:PlSqlParser.Over_clause_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#within_or_over_clause_keyword.
    def enterWithin_or_over_clause_keyword(self, ctx:PlSqlParser.Within_or_over_clause_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#within_or_over_clause_keyword.
    def exitWithin_or_over_clause_keyword(self, ctx:PlSqlParser.Within_or_over_clause_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#standard_prediction_function_keyword.
    def enterStandard_prediction_function_keyword(self, ctx:PlSqlParser.Standard_prediction_function_keywordContext):
        pass

    # Exit a parse tree produced by PlSqlParser#standard_prediction_function_keyword.
    def exitStandard_prediction_function_keyword(self, ctx:PlSqlParser.Standard_prediction_function_keywordContext):
        pass


    # Enter a parse tree produced by PlSqlParser#over_clause.
    def enterOver_clause(self, ctx:PlSqlParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#over_clause.
    def exitOver_clause(self, ctx:PlSqlParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_clause.
    def enterWindowing_clause(self, ctx:PlSqlParser.Windowing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_clause.
    def exitWindowing_clause(self, ctx:PlSqlParser.Windowing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_type.
    def enterWindowing_type(self, ctx:PlSqlParser.Windowing_typeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_type.
    def exitWindowing_type(self, ctx:PlSqlParser.Windowing_typeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#windowing_elements.
    def enterWindowing_elements(self, ctx:PlSqlParser.Windowing_elementsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#windowing_elements.
    def exitWindowing_elements(self, ctx:PlSqlParser.Windowing_elementsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_clause.
    def enterUsing_clause(self, ctx:PlSqlParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_clause.
    def exitUsing_clause(self, ctx:PlSqlParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#using_element.
    def enterUsing_element(self, ctx:PlSqlParser.Using_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#using_element.
    def exitUsing_element(self, ctx:PlSqlParser.Using_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collect_order_by_part.
    def enterCollect_order_by_part(self, ctx:PlSqlParser.Collect_order_by_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collect_order_by_part.
    def exitCollect_order_by_part(self, ctx:PlSqlParser.Collect_order_by_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#within_or_over_part.
    def enterWithin_or_over_part(self, ctx:PlSqlParser.Within_or_over_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#within_or_over_part.
    def exitWithin_or_over_part(self, ctx:PlSqlParser.Within_or_over_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#string_delimiter.
    def enterString_delimiter(self, ctx:PlSqlParser.String_delimiterContext):
        pass

    # Exit a parse tree produced by PlSqlParser#string_delimiter.
    def exitString_delimiter(self, ctx:PlSqlParser.String_delimiterContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cost_matrix_clause.
    def enterCost_matrix_clause(self, ctx:PlSqlParser.Cost_matrix_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cost_matrix_clause.
    def exitCost_matrix_clause(self, ctx:PlSqlParser.Cost_matrix_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_passing_clause.
    def enterXml_passing_clause(self, ctx:PlSqlParser.Xml_passing_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_passing_clause.
    def exitXml_passing_clause(self, ctx:PlSqlParser.Xml_passing_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_attributes_clause.
    def enterXml_attributes_clause(self, ctx:PlSqlParser.Xml_attributes_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_attributes_clause.
    def exitXml_attributes_clause(self, ctx:PlSqlParser.Xml_attributes_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_namespaces_clause.
    def enterXml_namespaces_clause(self, ctx:PlSqlParser.Xml_namespaces_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_namespaces_clause.
    def exitXml_namespaces_clause(self, ctx:PlSqlParser.Xml_namespaces_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_table_column.
    def enterXml_table_column(self, ctx:PlSqlParser.Xml_table_columnContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_table_column.
    def exitXml_table_column(self, ctx:PlSqlParser.Xml_table_columnContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_general_default_part.
    def enterXml_general_default_part(self, ctx:PlSqlParser.Xml_general_default_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_general_default_part.
    def exitXml_general_default_part(self, ctx:PlSqlParser.Xml_general_default_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_multiuse_expression_element.
    def enterXml_multiuse_expression_element(self, ctx:PlSqlParser.Xml_multiuse_expression_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_multiuse_expression_element.
    def exitXml_multiuse_expression_element(self, ctx:PlSqlParser.Xml_multiuse_expression_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlroot_param_version_part.
    def enterXmlroot_param_version_part(self, ctx:PlSqlParser.Xmlroot_param_version_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlroot_param_version_part.
    def exitXmlroot_param_version_part(self, ctx:PlSqlParser.Xmlroot_param_version_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlroot_param_standalone_part.
    def enterXmlroot_param_standalone_part(self, ctx:PlSqlParser.Xmlroot_param_standalone_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlroot_param_standalone_part.
    def exitXmlroot_param_standalone_part(self, ctx:PlSqlParser.Xmlroot_param_standalone_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_enconding_part.
    def enterXmlserialize_param_enconding_part(self, ctx:PlSqlParser.Xmlserialize_param_enconding_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_enconding_part.
    def exitXmlserialize_param_enconding_part(self, ctx:PlSqlParser.Xmlserialize_param_enconding_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_version_part.
    def enterXmlserialize_param_version_part(self, ctx:PlSqlParser.Xmlserialize_param_version_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_version_part.
    def exitXmlserialize_param_version_part(self, ctx:PlSqlParser.Xmlserialize_param_version_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmlserialize_param_ident_part.
    def enterXmlserialize_param_ident_part(self, ctx:PlSqlParser.Xmlserialize_param_ident_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmlserialize_param_ident_part.
    def exitXmlserialize_param_ident_part(self, ctx:PlSqlParser.Xmlserialize_param_ident_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_plus_command_no_semicolon.
    def enterSql_plus_command_no_semicolon(self, ctx:PlSqlParser.Sql_plus_command_no_semicolonContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_plus_command_no_semicolon.
    def exitSql_plus_command_no_semicolon(self, ctx:PlSqlParser.Sql_plus_command_no_semicolonContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sql_plus_command.
    def enterSql_plus_command(self, ctx:PlSqlParser.Sql_plus_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sql_plus_command.
    def exitSql_plus_command(self, ctx:PlSqlParser.Sql_plus_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#start_command.
    def enterStart_command(self, ctx:PlSqlParser.Start_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#start_command.
    def exitStart_command(self, ctx:PlSqlParser.Start_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#whenever_command.
    def enterWhenever_command(self, ctx:PlSqlParser.Whenever_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#whenever_command.
    def exitWhenever_command(self, ctx:PlSqlParser.Whenever_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#set_command.
    def enterSet_command(self, ctx:PlSqlParser.Set_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#set_command.
    def exitSet_command(self, ctx:PlSqlParser.Set_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#timing_command.
    def enterTiming_command(self, ctx:PlSqlParser.Timing_commandContext):
        pass

    # Exit a parse tree produced by PlSqlParser#timing_command.
    def exitTiming_command(self, ctx:PlSqlParser.Timing_commandContext):
        pass


    # Enter a parse tree produced by PlSqlParser#partition_extension_clause.
    def enterPartition_extension_clause(self, ctx:PlSqlParser.Partition_extension_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#partition_extension_clause.
    def exitPartition_extension_clause(self, ctx:PlSqlParser.Partition_extension_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_alias.
    def enterColumn_alias(self, ctx:PlSqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_alias.
    def exitColumn_alias(self, ctx:PlSqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_alias.
    def enterTable_alias(self, ctx:PlSqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_alias.
    def exitTable_alias(self, ctx:PlSqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by PlSqlParser#where_clause.
    def enterWhere_clause(self, ctx:PlSqlParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#where_clause.
    def exitWhere_clause(self, ctx:PlSqlParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quantitative_where_stmt.
    def enterQuantitative_where_stmt(self, ctx:PlSqlParser.Quantitative_where_stmtContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quantitative_where_stmt.
    def exitQuantitative_where_stmt(self, ctx:PlSqlParser.Quantitative_where_stmtContext):
        pass


    # Enter a parse tree produced by PlSqlParser#into_clause.
    def enterInto_clause(self, ctx:PlSqlParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#into_clause.
    def exitInto_clause(self, ctx:PlSqlParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xml_column_name.
    def enterXml_column_name(self, ctx:PlSqlParser.Xml_column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xml_column_name.
    def exitXml_column_name(self, ctx:PlSqlParser.Xml_column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cost_class_name.
    def enterCost_class_name(self, ctx:PlSqlParser.Cost_class_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cost_class_name.
    def exitCost_class_name(self, ctx:PlSqlParser.Cost_class_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#attribute_name.
    def enterAttribute_name(self, ctx:PlSqlParser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#attribute_name.
    def exitAttribute_name(self, ctx:PlSqlParser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#savepoint_name.
    def enterSavepoint_name(self, ctx:PlSqlParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#savepoint_name.
    def exitSavepoint_name(self, ctx:PlSqlParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#rollback_segment_name.
    def enterRollback_segment_name(self, ctx:PlSqlParser.Rollback_segment_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#rollback_segment_name.
    def exitRollback_segment_name(self, ctx:PlSqlParser.Rollback_segment_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_var_name.
    def enterTable_var_name(self, ctx:PlSqlParser.Table_var_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_var_name.
    def exitTable_var_name(self, ctx:PlSqlParser.Table_var_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#schema_name.
    def enterSchema_name(self, ctx:PlSqlParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#schema_name.
    def exitSchema_name(self, ctx:PlSqlParser.Schema_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#routine_name.
    def enterRoutine_name(self, ctx:PlSqlParser.Routine_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#routine_name.
    def exitRoutine_name(self, ctx:PlSqlParser.Routine_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#package_name.
    def enterPackage_name(self, ctx:PlSqlParser.Package_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#package_name.
    def exitPackage_name(self, ctx:PlSqlParser.Package_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#implementation_type_name.
    def enterImplementation_type_name(self, ctx:PlSqlParser.Implementation_type_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#implementation_type_name.
    def exitImplementation_type_name(self, ctx:PlSqlParser.Implementation_type_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#parameter_name.
    def enterParameter_name(self, ctx:PlSqlParser.Parameter_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#parameter_name.
    def exitParameter_name(self, ctx:PlSqlParser.Parameter_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#reference_model_name.
    def enterReference_model_name(self, ctx:PlSqlParser.Reference_model_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#reference_model_name.
    def exitReference_model_name(self, ctx:PlSqlParser.Reference_model_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#main_model_name.
    def enterMain_model_name(self, ctx:PlSqlParser.Main_model_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#main_model_name.
    def exitMain_model_name(self, ctx:PlSqlParser.Main_model_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#container_tableview_name.
    def enterContainer_tableview_name(self, ctx:PlSqlParser.Container_tableview_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#container_tableview_name.
    def exitContainer_tableview_name(self, ctx:PlSqlParser.Container_tableview_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#aggregate_function_name.
    def enterAggregate_function_name(self, ctx:PlSqlParser.Aggregate_function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#aggregate_function_name.
    def exitAggregate_function_name(self, ctx:PlSqlParser.Aggregate_function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#query_name.
    def enterQuery_name(self, ctx:PlSqlParser.Query_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#query_name.
    def exitQuery_name(self, ctx:PlSqlParser.Query_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grantee_name.
    def enterGrantee_name(self, ctx:PlSqlParser.Grantee_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grantee_name.
    def exitGrantee_name(self, ctx:PlSqlParser.Grantee_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#role_name.
    def enterRole_name(self, ctx:PlSqlParser.Role_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#role_name.
    def exitRole_name(self, ctx:PlSqlParser.Role_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constraint_name.
    def enterConstraint_name(self, ctx:PlSqlParser.Constraint_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constraint_name.
    def exitConstraint_name(self, ctx:PlSqlParser.Constraint_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#label_name.
    def enterLabel_name(self, ctx:PlSqlParser.Label_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#label_name.
    def exitLabel_name(self, ctx:PlSqlParser.Label_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_name.
    def enterType_name(self, ctx:PlSqlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_name.
    def exitType_name(self, ctx:PlSqlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#sequence_name.
    def enterSequence_name(self, ctx:PlSqlParser.Sequence_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#sequence_name.
    def exitSequence_name(self, ctx:PlSqlParser.Sequence_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#exception_name.
    def enterException_name(self, ctx:PlSqlParser.Exception_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#exception_name.
    def exitException_name(self, ctx:PlSqlParser.Exception_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_name.
    def enterFunction_name(self, ctx:PlSqlParser.Function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_name.
    def exitFunction_name(self, ctx:PlSqlParser.Function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#procedure_name.
    def enterProcedure_name(self, ctx:PlSqlParser.Procedure_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#procedure_name.
    def exitProcedure_name(self, ctx:PlSqlParser.Procedure_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#trigger_name.
    def enterTrigger_name(self, ctx:PlSqlParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#trigger_name.
    def exitTrigger_name(self, ctx:PlSqlParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#variable_name.
    def enterVariable_name(self, ctx:PlSqlParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#variable_name.
    def exitVariable_name(self, ctx:PlSqlParser.Variable_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#index_name.
    def enterIndex_name(self, ctx:PlSqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#index_name.
    def exitIndex_name(self, ctx:PlSqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#cursor_name.
    def enterCursor_name(self, ctx:PlSqlParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#cursor_name.
    def exitCursor_name(self, ctx:PlSqlParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#record_name.
    def enterRecord_name(self, ctx:PlSqlParser.Record_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#record_name.
    def exitRecord_name(self, ctx:PlSqlParser.Record_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#collection_name.
    def enterCollection_name(self, ctx:PlSqlParser.Collection_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#collection_name.
    def exitCollection_name(self, ctx:PlSqlParser.Collection_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#link_name.
    def enterLink_name(self, ctx:PlSqlParser.Link_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#link_name.
    def exitLink_name(self, ctx:PlSqlParser.Link_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#local_link_name.
    def enterLocal_link_name(self, ctx:PlSqlParser.Local_link_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#local_link_name.
    def exitLocal_link_name(self, ctx:PlSqlParser.Local_link_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#connection_qualifier.
    def enterConnection_qualifier(self, ctx:PlSqlParser.Connection_qualifierContext):
        pass

    # Exit a parse tree produced by PlSqlParser#connection_qualifier.
    def exitConnection_qualifier(self, ctx:PlSqlParser.Connection_qualifierContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_name.
    def enterColumn_name(self, ctx:PlSqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_name.
    def exitColumn_name(self, ctx:PlSqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#tableview_name.
    def enterTableview_name(self, ctx:PlSqlParser.Tableview_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#tableview_name.
    def exitTableview_name(self, ctx:PlSqlParser.Tableview_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#xmltable.
    def enterXmltable(self, ctx:PlSqlParser.XmltableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#xmltable.
    def exitXmltable(self, ctx:PlSqlParser.XmltableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#char_set_name.
    def enterChar_set_name(self, ctx:PlSqlParser.Char_set_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#char_set_name.
    def exitChar_set_name(self, ctx:PlSqlParser.Char_set_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#synonym_name.
    def enterSynonym_name(self, ctx:PlSqlParser.Synonym_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#synonym_name.
    def exitSynonym_name(self, ctx:PlSqlParser.Synonym_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#schema_object_name.
    def enterSchema_object_name(self, ctx:PlSqlParser.Schema_object_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#schema_object_name.
    def exitSchema_object_name(self, ctx:PlSqlParser.Schema_object_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#dir_object_name.
    def enterDir_object_name(self, ctx:PlSqlParser.Dir_object_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#dir_object_name.
    def exitDir_object_name(self, ctx:PlSqlParser.Dir_object_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#user_object_name.
    def enterUser_object_name(self, ctx:PlSqlParser.User_object_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#user_object_name.
    def exitUser_object_name(self, ctx:PlSqlParser.User_object_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#grant_object_name.
    def enterGrant_object_name(self, ctx:PlSqlParser.Grant_object_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#grant_object_name.
    def exitGrant_object_name(self, ctx:PlSqlParser.Grant_object_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#column_list.
    def enterColumn_list(self, ctx:PlSqlParser.Column_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#column_list.
    def exitColumn_list(self, ctx:PlSqlParser.Column_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#paren_column_list.
    def enterParen_column_list(self, ctx:PlSqlParser.Paren_column_listContext):
        pass

    # Exit a parse tree produced by PlSqlParser#paren_column_list.
    def exitParen_column_list(self, ctx:PlSqlParser.Paren_column_listContext):
        pass


    # Enter a parse tree produced by PlSqlParser#keep_clause.
    def enterKeep_clause(self, ctx:PlSqlParser.Keep_clauseContext):
        pass

    # Exit a parse tree produced by PlSqlParser#keep_clause.
    def exitKeep_clause(self, ctx:PlSqlParser.Keep_clauseContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument.
    def enterFunction_argument(self, ctx:PlSqlParser.Function_argumentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument.
    def exitFunction_argument(self, ctx:PlSqlParser.Function_argumentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument_analytic.
    def enterFunction_argument_analytic(self, ctx:PlSqlParser.Function_argument_analyticContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument_analytic.
    def exitFunction_argument_analytic(self, ctx:PlSqlParser.Function_argument_analyticContext):
        pass


    # Enter a parse tree produced by PlSqlParser#function_argument_modeling.
    def enterFunction_argument_modeling(self, ctx:PlSqlParser.Function_argument_modelingContext):
        pass

    # Exit a parse tree produced by PlSqlParser#function_argument_modeling.
    def exitFunction_argument_modeling(self, ctx:PlSqlParser.Function_argument_modelingContext):
        pass


    # Enter a parse tree produced by PlSqlParser#respect_or_ignore_nulls.
    def enterRespect_or_ignore_nulls(self, ctx:PlSqlParser.Respect_or_ignore_nullsContext):
        pass

    # Exit a parse tree produced by PlSqlParser#respect_or_ignore_nulls.
    def exitRespect_or_ignore_nulls(self, ctx:PlSqlParser.Respect_or_ignore_nullsContext):
        pass


    # Enter a parse tree produced by PlSqlParser#argument.
    def enterArgument(self, ctx:PlSqlParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PlSqlParser#argument.
    def exitArgument(self, ctx:PlSqlParser.ArgumentContext):
        pass


    # Enter a parse tree produced by PlSqlParser#type_spec.
    def enterType_spec(self, ctx:PlSqlParser.Type_specContext):
        pass

    # Exit a parse tree produced by PlSqlParser#type_spec.
    def exitType_spec(self, ctx:PlSqlParser.Type_specContext):
        pass


    # Enter a parse tree produced by PlSqlParser#datatype.
    def enterDatatype(self, ctx:PlSqlParser.DatatypeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#datatype.
    def exitDatatype(self, ctx:PlSqlParser.DatatypeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#precision_part.
    def enterPrecision_part(self, ctx:PlSqlParser.Precision_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#precision_part.
    def exitPrecision_part(self, ctx:PlSqlParser.Precision_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#native_datatype_element.
    def enterNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#native_datatype_element.
    def exitNative_datatype_element(self, ctx:PlSqlParser.Native_datatype_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#bind_variable.
    def enterBind_variable(self, ctx:PlSqlParser.Bind_variableContext):
        pass

    # Exit a parse tree produced by PlSqlParser#bind_variable.
    def exitBind_variable(self, ctx:PlSqlParser.Bind_variableContext):
        pass


    # Enter a parse tree produced by PlSqlParser#general_element.
    def enterGeneral_element(self, ctx:PlSqlParser.General_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#general_element.
    def exitGeneral_element(self, ctx:PlSqlParser.General_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#general_element_part.
    def enterGeneral_element_part(self, ctx:PlSqlParser.General_element_partContext):
        pass

    # Exit a parse tree produced by PlSqlParser#general_element_part.
    def exitGeneral_element_part(self, ctx:PlSqlParser.General_element_partContext):
        pass


    # Enter a parse tree produced by PlSqlParser#table_element.
    def enterTable_element(self, ctx:PlSqlParser.Table_elementContext):
        pass

    # Exit a parse tree produced by PlSqlParser#table_element.
    def exitTable_element(self, ctx:PlSqlParser.Table_elementContext):
        pass


    # Enter a parse tree produced by PlSqlParser#object_privilege.
    def enterObject_privilege(self, ctx:PlSqlParser.Object_privilegeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#object_privilege.
    def exitObject_privilege(self, ctx:PlSqlParser.Object_privilegeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#system_privilege.
    def enterSystem_privilege(self, ctx:PlSqlParser.System_privilegeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#system_privilege.
    def exitSystem_privilege(self, ctx:PlSqlParser.System_privilegeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#constant.
    def enterConstant(self, ctx:PlSqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by PlSqlParser#constant.
    def exitConstant(self, ctx:PlSqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric.
    def enterNumeric(self, ctx:PlSqlParser.NumericContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric.
    def exitNumeric(self, ctx:PlSqlParser.NumericContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric_negative.
    def enterNumeric_negative(self, ctx:PlSqlParser.Numeric_negativeContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric_negative.
    def exitNumeric_negative(self, ctx:PlSqlParser.Numeric_negativeContext):
        pass


    # Enter a parse tree produced by PlSqlParser#quoted_string.
    def enterQuoted_string(self, ctx:PlSqlParser.Quoted_stringContext):
        pass

    # Exit a parse tree produced by PlSqlParser#quoted_string.
    def exitQuoted_string(self, ctx:PlSqlParser.Quoted_stringContext):
        pass


    # Enter a parse tree produced by PlSqlParser#identifier.
    def enterIdentifier(self, ctx:PlSqlParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PlSqlParser#identifier.
    def exitIdentifier(self, ctx:PlSqlParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PlSqlParser#id_expression.
    def enterId_expression(self, ctx:PlSqlParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by PlSqlParser#id_expression.
    def exitId_expression(self, ctx:PlSqlParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by PlSqlParser#inquiry_directive.
    def enterInquiry_directive(self, ctx:PlSqlParser.Inquiry_directiveContext):
        pass

    # Exit a parse tree produced by PlSqlParser#inquiry_directive.
    def exitInquiry_directive(self, ctx:PlSqlParser.Inquiry_directiveContext):
        pass


    # Enter a parse tree produced by PlSqlParser#outer_join_sign.
    def enterOuter_join_sign(self, ctx:PlSqlParser.Outer_join_signContext):
        pass

    # Exit a parse tree produced by PlSqlParser#outer_join_sign.
    def exitOuter_join_sign(self, ctx:PlSqlParser.Outer_join_signContext):
        pass


    # Enter a parse tree produced by PlSqlParser#regular_id.
    def enterRegular_id(self, ctx:PlSqlParser.Regular_idContext):
        pass

    # Exit a parse tree produced by PlSqlParser#regular_id.
    def exitRegular_id(self, ctx:PlSqlParser.Regular_idContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_reserved_keywords_in_18c.
    def enterNon_reserved_keywords_in_18c(self, ctx:PlSqlParser.Non_reserved_keywords_in_18cContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_reserved_keywords_in_18c.
    def exitNon_reserved_keywords_in_18c(self, ctx:PlSqlParser.Non_reserved_keywords_in_18cContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_reserved_keywords_in_12c.
    def enterNon_reserved_keywords_in_12c(self, ctx:PlSqlParser.Non_reserved_keywords_in_12cContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_reserved_keywords_in_12c.
    def exitNon_reserved_keywords_in_12c(self, ctx:PlSqlParser.Non_reserved_keywords_in_12cContext):
        pass


    # Enter a parse tree produced by PlSqlParser#non_reserved_keywords_pre12c.
    def enterNon_reserved_keywords_pre12c(self, ctx:PlSqlParser.Non_reserved_keywords_pre12cContext):
        pass

    # Exit a parse tree produced by PlSqlParser#non_reserved_keywords_pre12c.
    def exitNon_reserved_keywords_pre12c(self, ctx:PlSqlParser.Non_reserved_keywords_pre12cContext):
        pass


    # Enter a parse tree produced by PlSqlParser#string_function_name.
    def enterString_function_name(self, ctx:PlSqlParser.String_function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#string_function_name.
    def exitString_function_name(self, ctx:PlSqlParser.String_function_nameContext):
        pass


    # Enter a parse tree produced by PlSqlParser#numeric_function_name.
    def enterNumeric_function_name(self, ctx:PlSqlParser.Numeric_function_nameContext):
        pass

    # Exit a parse tree produced by PlSqlParser#numeric_function_name.
    def exitNumeric_function_name(self, ctx:PlSqlParser.Numeric_function_nameContext):
        pass



del PlSqlParser