# Generated from /data/Coding/LLM4DB/antlr_gram/pg/PostgreSQLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser



# This class defines a complete listener for a parse tree produced by PostgreSQLParser.
class PostgreSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by PostgreSQLParser#root.
    def enterRoot(self, ctx:PostgreSQLParser.RootContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#root.
    def exitRoot(self, ctx:PostgreSQLParser.RootContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsqlroot.
    def enterPlsqlroot(self, ctx:PostgreSQLParser.PlsqlrootContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsqlroot.
    def exitPlsqlroot(self, ctx:PostgreSQLParser.PlsqlrootContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmtblock.
    def enterStmtblock(self, ctx:PostgreSQLParser.StmtblockContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmtblock.
    def exitStmtblock(self, ctx:PostgreSQLParser.StmtblockContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmtmulti.
    def enterStmtmulti(self, ctx:PostgreSQLParser.StmtmultiContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmtmulti.
    def exitStmtmulti(self, ctx:PostgreSQLParser.StmtmultiContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt.
    def enterStmt(self, ctx:PostgreSQLParser.StmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt.
    def exitStmt(self, ctx:PostgreSQLParser.StmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsqlconsolecommand.
    def enterPlsqlconsolecommand(self, ctx:PostgreSQLParser.PlsqlconsolecommandContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsqlconsolecommand.
    def exitPlsqlconsolecommand(self, ctx:PostgreSQLParser.PlsqlconsolecommandContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#callstmt.
    def enterCallstmt(self, ctx:PostgreSQLParser.CallstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#callstmt.
    def exitCallstmt(self, ctx:PostgreSQLParser.CallstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createrolestmt.
    def enterCreaterolestmt(self, ctx:PostgreSQLParser.CreaterolestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createrolestmt.
    def exitCreaterolestmt(self, ctx:PostgreSQLParser.CreaterolestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_with.
    def enterOpt_with(self, ctx:PostgreSQLParser.Opt_withContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_with.
    def exitOpt_with(self, ctx:PostgreSQLParser.Opt_withContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optrolelist.
    def enterOptrolelist(self, ctx:PostgreSQLParser.OptrolelistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optrolelist.
    def exitOptrolelist(self, ctx:PostgreSQLParser.OptrolelistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alteroptrolelist.
    def enterAlteroptrolelist(self, ctx:PostgreSQLParser.AlteroptrolelistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alteroptrolelist.
    def exitAlteroptrolelist(self, ctx:PostgreSQLParser.AlteroptrolelistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alteroptroleelem.
    def enterAlteroptroleelem(self, ctx:PostgreSQLParser.AlteroptroleelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alteroptroleelem.
    def exitAlteroptroleelem(self, ctx:PostgreSQLParser.AlteroptroleelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createoptroleelem.
    def enterCreateoptroleelem(self, ctx:PostgreSQLParser.CreateoptroleelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createoptroleelem.
    def exitCreateoptroleelem(self, ctx:PostgreSQLParser.CreateoptroleelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createuserstmt.
    def enterCreateuserstmt(self, ctx:PostgreSQLParser.CreateuserstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createuserstmt.
    def exitCreateuserstmt(self, ctx:PostgreSQLParser.CreateuserstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterrolestmt.
    def enterAlterrolestmt(self, ctx:PostgreSQLParser.AlterrolestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterrolestmt.
    def exitAlterrolestmt(self, ctx:PostgreSQLParser.AlterrolestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_in_database.
    def enterOpt_in_database(self, ctx:PostgreSQLParser.Opt_in_databaseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_in_database.
    def exitOpt_in_database(self, ctx:PostgreSQLParser.Opt_in_databaseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterrolesetstmt.
    def enterAlterrolesetstmt(self, ctx:PostgreSQLParser.AlterrolesetstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterrolesetstmt.
    def exitAlterrolesetstmt(self, ctx:PostgreSQLParser.AlterrolesetstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#droprolestmt.
    def enterDroprolestmt(self, ctx:PostgreSQLParser.DroprolestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#droprolestmt.
    def exitDroprolestmt(self, ctx:PostgreSQLParser.DroprolestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#creategroupstmt.
    def enterCreategroupstmt(self, ctx:PostgreSQLParser.CreategroupstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#creategroupstmt.
    def exitCreategroupstmt(self, ctx:PostgreSQLParser.CreategroupstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altergroupstmt.
    def enterAltergroupstmt(self, ctx:PostgreSQLParser.AltergroupstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altergroupstmt.
    def exitAltergroupstmt(self, ctx:PostgreSQLParser.AltergroupstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#add_drop.
    def enterAdd_drop(self, ctx:PostgreSQLParser.Add_dropContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#add_drop.
    def exitAdd_drop(self, ctx:PostgreSQLParser.Add_dropContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createschemastmt.
    def enterCreateschemastmt(self, ctx:PostgreSQLParser.CreateschemastmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createschemastmt.
    def exitCreateschemastmt(self, ctx:PostgreSQLParser.CreateschemastmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optschemaname.
    def enterOptschemaname(self, ctx:PostgreSQLParser.OptschemanameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optschemaname.
    def exitOptschemaname(self, ctx:PostgreSQLParser.OptschemanameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optschemaeltlist.
    def enterOptschemaeltlist(self, ctx:PostgreSQLParser.OptschemaeltlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optschemaeltlist.
    def exitOptschemaeltlist(self, ctx:PostgreSQLParser.OptschemaeltlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#schema_stmt.
    def enterSchema_stmt(self, ctx:PostgreSQLParser.Schema_stmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#schema_stmt.
    def exitSchema_stmt(self, ctx:PostgreSQLParser.Schema_stmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#variablesetstmt.
    def enterVariablesetstmt(self, ctx:PostgreSQLParser.VariablesetstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#variablesetstmt.
    def exitVariablesetstmt(self, ctx:PostgreSQLParser.VariablesetstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_rest.
    def enterSet_rest(self, ctx:PostgreSQLParser.Set_restContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_rest.
    def exitSet_rest(self, ctx:PostgreSQLParser.Set_restContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_set.
    def enterGeneric_set(self, ctx:PostgreSQLParser.Generic_setContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_set.
    def exitGeneric_set(self, ctx:PostgreSQLParser.Generic_setContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_rest_more.
    def enterSet_rest_more(self, ctx:PostgreSQLParser.Set_rest_moreContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_rest_more.
    def exitSet_rest_more(self, ctx:PostgreSQLParser.Set_rest_moreContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#var_name.
    def enterVar_name(self, ctx:PostgreSQLParser.Var_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#var_name.
    def exitVar_name(self, ctx:PostgreSQLParser.Var_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#var_list.
    def enterVar_list(self, ctx:PostgreSQLParser.Var_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#var_list.
    def exitVar_list(self, ctx:PostgreSQLParser.Var_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#var_value.
    def enterVar_value(self, ctx:PostgreSQLParser.Var_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#var_value.
    def exitVar_value(self, ctx:PostgreSQLParser.Var_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#iso_level.
    def enterIso_level(self, ctx:PostgreSQLParser.Iso_levelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#iso_level.
    def exitIso_level(self, ctx:PostgreSQLParser.Iso_levelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_boolean_or_string.
    def enterOpt_boolean_or_string(self, ctx:PostgreSQLParser.Opt_boolean_or_stringContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_boolean_or_string.
    def exitOpt_boolean_or_string(self, ctx:PostgreSQLParser.Opt_boolean_or_stringContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#zone_value.
    def enterZone_value(self, ctx:PostgreSQLParser.Zone_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#zone_value.
    def exitZone_value(self, ctx:PostgreSQLParser.Zone_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_encoding.
    def enterOpt_encoding(self, ctx:PostgreSQLParser.Opt_encodingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_encoding.
    def exitOpt_encoding(self, ctx:PostgreSQLParser.Opt_encodingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#nonreservedword_or_sconst.
    def enterNonreservedword_or_sconst(self, ctx:PostgreSQLParser.Nonreservedword_or_sconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#nonreservedword_or_sconst.
    def exitNonreservedword_or_sconst(self, ctx:PostgreSQLParser.Nonreservedword_or_sconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#variableresetstmt.
    def enterVariableresetstmt(self, ctx:PostgreSQLParser.VariableresetstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#variableresetstmt.
    def exitVariableresetstmt(self, ctx:PostgreSQLParser.VariableresetstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reset_rest.
    def enterReset_rest(self, ctx:PostgreSQLParser.Reset_restContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reset_rest.
    def exitReset_rest(self, ctx:PostgreSQLParser.Reset_restContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_reset.
    def enterGeneric_reset(self, ctx:PostgreSQLParser.Generic_resetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_reset.
    def exitGeneric_reset(self, ctx:PostgreSQLParser.Generic_resetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#setresetclause.
    def enterSetresetclause(self, ctx:PostgreSQLParser.SetresetclauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#setresetclause.
    def exitSetresetclause(self, ctx:PostgreSQLParser.SetresetclauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#functionsetresetclause.
    def enterFunctionsetresetclause(self, ctx:PostgreSQLParser.FunctionsetresetclauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#functionsetresetclause.
    def exitFunctionsetresetclause(self, ctx:PostgreSQLParser.FunctionsetresetclauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#variableshowstmt.
    def enterVariableshowstmt(self, ctx:PostgreSQLParser.VariableshowstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#variableshowstmt.
    def exitVariableshowstmt(self, ctx:PostgreSQLParser.VariableshowstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraintssetstmt.
    def enterConstraintssetstmt(self, ctx:PostgreSQLParser.ConstraintssetstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraintssetstmt.
    def exitConstraintssetstmt(self, ctx:PostgreSQLParser.ConstraintssetstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraints_set_list.
    def enterConstraints_set_list(self, ctx:PostgreSQLParser.Constraints_set_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraints_set_list.
    def exitConstraints_set_list(self, ctx:PostgreSQLParser.Constraints_set_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraints_set_mode.
    def enterConstraints_set_mode(self, ctx:PostgreSQLParser.Constraints_set_modeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraints_set_mode.
    def exitConstraints_set_mode(self, ctx:PostgreSQLParser.Constraints_set_modeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#checkpointstmt.
    def enterCheckpointstmt(self, ctx:PostgreSQLParser.CheckpointstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#checkpointstmt.
    def exitCheckpointstmt(self, ctx:PostgreSQLParser.CheckpointstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#discardstmt.
    def enterDiscardstmt(self, ctx:PostgreSQLParser.DiscardstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#discardstmt.
    def exitDiscardstmt(self, ctx:PostgreSQLParser.DiscardstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altertablestmt.
    def enterAltertablestmt(self, ctx:PostgreSQLParser.AltertablestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altertablestmt.
    def exitAltertablestmt(self, ctx:PostgreSQLParser.AltertablestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_table_cmds.
    def enterAlter_table_cmds(self, ctx:PostgreSQLParser.Alter_table_cmdsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_table_cmds.
    def exitAlter_table_cmds(self, ctx:PostgreSQLParser.Alter_table_cmdsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#partition_cmd.
    def enterPartition_cmd(self, ctx:PostgreSQLParser.Partition_cmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#partition_cmd.
    def exitPartition_cmd(self, ctx:PostgreSQLParser.Partition_cmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#index_partition_cmd.
    def enterIndex_partition_cmd(self, ctx:PostgreSQLParser.Index_partition_cmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#index_partition_cmd.
    def exitIndex_partition_cmd(self, ctx:PostgreSQLParser.Index_partition_cmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_table_cmd.
    def enterAlter_table_cmd(self, ctx:PostgreSQLParser.Alter_table_cmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_table_cmd.
    def exitAlter_table_cmd(self, ctx:PostgreSQLParser.Alter_table_cmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_column_default.
    def enterAlter_column_default(self, ctx:PostgreSQLParser.Alter_column_defaultContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_column_default.
    def exitAlter_column_default(self, ctx:PostgreSQLParser.Alter_column_defaultContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_drop_behavior.
    def enterOpt_drop_behavior(self, ctx:PostgreSQLParser.Opt_drop_behaviorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_drop_behavior.
    def exitOpt_drop_behavior(self, ctx:PostgreSQLParser.Opt_drop_behaviorContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_collate_clause.
    def enterOpt_collate_clause(self, ctx:PostgreSQLParser.Opt_collate_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_collate_clause.
    def exitOpt_collate_clause(self, ctx:PostgreSQLParser.Opt_collate_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_using.
    def enterAlter_using(self, ctx:PostgreSQLParser.Alter_usingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_using.
    def exitAlter_using(self, ctx:PostgreSQLParser.Alter_usingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#replica_identity.
    def enterReplica_identity(self, ctx:PostgreSQLParser.Replica_identityContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#replica_identity.
    def exitReplica_identity(self, ctx:PostgreSQLParser.Replica_identityContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reloptions.
    def enterReloptions(self, ctx:PostgreSQLParser.ReloptionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reloptions.
    def exitReloptions(self, ctx:PostgreSQLParser.ReloptionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_reloptions.
    def enterOpt_reloptions(self, ctx:PostgreSQLParser.Opt_reloptionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_reloptions.
    def exitOpt_reloptions(self, ctx:PostgreSQLParser.Opt_reloptionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reloption_list.
    def enterReloption_list(self, ctx:PostgreSQLParser.Reloption_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reloption_list.
    def exitReloption_list(self, ctx:PostgreSQLParser.Reloption_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reloption_elem.
    def enterReloption_elem(self, ctx:PostgreSQLParser.Reloption_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reloption_elem.
    def exitReloption_elem(self, ctx:PostgreSQLParser.Reloption_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_identity_column_option_list.
    def enterAlter_identity_column_option_list(self, ctx:PostgreSQLParser.Alter_identity_column_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_identity_column_option_list.
    def exitAlter_identity_column_option_list(self, ctx:PostgreSQLParser.Alter_identity_column_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_identity_column_option.
    def enterAlter_identity_column_option(self, ctx:PostgreSQLParser.Alter_identity_column_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_identity_column_option.
    def exitAlter_identity_column_option(self, ctx:PostgreSQLParser.Alter_identity_column_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#partitionboundspec.
    def enterPartitionboundspec(self, ctx:PostgreSQLParser.PartitionboundspecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#partitionboundspec.
    def exitPartitionboundspec(self, ctx:PostgreSQLParser.PartitionboundspecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#hash_partbound_elem.
    def enterHash_partbound_elem(self, ctx:PostgreSQLParser.Hash_partbound_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#hash_partbound_elem.
    def exitHash_partbound_elem(self, ctx:PostgreSQLParser.Hash_partbound_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#hash_partbound.
    def enterHash_partbound(self, ctx:PostgreSQLParser.Hash_partboundContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#hash_partbound.
    def exitHash_partbound(self, ctx:PostgreSQLParser.Hash_partboundContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altercompositetypestmt.
    def enterAltercompositetypestmt(self, ctx:PostgreSQLParser.AltercompositetypestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altercompositetypestmt.
    def exitAltercompositetypestmt(self, ctx:PostgreSQLParser.AltercompositetypestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_type_cmds.
    def enterAlter_type_cmds(self, ctx:PostgreSQLParser.Alter_type_cmdsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_type_cmds.
    def exitAlter_type_cmds(self, ctx:PostgreSQLParser.Alter_type_cmdsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_type_cmd.
    def enterAlter_type_cmd(self, ctx:PostgreSQLParser.Alter_type_cmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_type_cmd.
    def exitAlter_type_cmd(self, ctx:PostgreSQLParser.Alter_type_cmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#closeportalstmt.
    def enterCloseportalstmt(self, ctx:PostgreSQLParser.CloseportalstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#closeportalstmt.
    def exitCloseportalstmt(self, ctx:PostgreSQLParser.CloseportalstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copystmt.
    def enterCopystmt(self, ctx:PostgreSQLParser.CopystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copystmt.
    def exitCopystmt(self, ctx:PostgreSQLParser.CopystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_from.
    def enterCopy_from(self, ctx:PostgreSQLParser.Copy_fromContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_from.
    def exitCopy_from(self, ctx:PostgreSQLParser.Copy_fromContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_program.
    def enterOpt_program(self, ctx:PostgreSQLParser.Opt_programContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_program.
    def exitOpt_program(self, ctx:PostgreSQLParser.Opt_programContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_file_name.
    def enterCopy_file_name(self, ctx:PostgreSQLParser.Copy_file_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_file_name.
    def exitCopy_file_name(self, ctx:PostgreSQLParser.Copy_file_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_options.
    def enterCopy_options(self, ctx:PostgreSQLParser.Copy_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_options.
    def exitCopy_options(self, ctx:PostgreSQLParser.Copy_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_opt_list.
    def enterCopy_opt_list(self, ctx:PostgreSQLParser.Copy_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_opt_list.
    def exitCopy_opt_list(self, ctx:PostgreSQLParser.Copy_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_opt_item.
    def enterCopy_opt_item(self, ctx:PostgreSQLParser.Copy_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_opt_item.
    def exitCopy_opt_item(self, ctx:PostgreSQLParser.Copy_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_binary.
    def enterOpt_binary(self, ctx:PostgreSQLParser.Opt_binaryContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_binary.
    def exitOpt_binary(self, ctx:PostgreSQLParser.Opt_binaryContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_delimiter.
    def enterCopy_delimiter(self, ctx:PostgreSQLParser.Copy_delimiterContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_delimiter.
    def exitCopy_delimiter(self, ctx:PostgreSQLParser.Copy_delimiterContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_using.
    def enterOpt_using(self, ctx:PostgreSQLParser.Opt_usingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_using.
    def exitOpt_using(self, ctx:PostgreSQLParser.Opt_usingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_generic_opt_list.
    def enterCopy_generic_opt_list(self, ctx:PostgreSQLParser.Copy_generic_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_generic_opt_list.
    def exitCopy_generic_opt_list(self, ctx:PostgreSQLParser.Copy_generic_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_generic_opt_elem.
    def enterCopy_generic_opt_elem(self, ctx:PostgreSQLParser.Copy_generic_opt_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_generic_opt_elem.
    def exitCopy_generic_opt_elem(self, ctx:PostgreSQLParser.Copy_generic_opt_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_generic_opt_arg.
    def enterCopy_generic_opt_arg(self, ctx:PostgreSQLParser.Copy_generic_opt_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_generic_opt_arg.
    def exitCopy_generic_opt_arg(self, ctx:PostgreSQLParser.Copy_generic_opt_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_generic_opt_arg_list.
    def enterCopy_generic_opt_arg_list(self, ctx:PostgreSQLParser.Copy_generic_opt_arg_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_generic_opt_arg_list.
    def exitCopy_generic_opt_arg_list(self, ctx:PostgreSQLParser.Copy_generic_opt_arg_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#copy_generic_opt_arg_list_item.
    def enterCopy_generic_opt_arg_list_item(self, ctx:PostgreSQLParser.Copy_generic_opt_arg_list_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#copy_generic_opt_arg_list_item.
    def exitCopy_generic_opt_arg_list_item(self, ctx:PostgreSQLParser.Copy_generic_opt_arg_list_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createstmt.
    def enterCreatestmt(self, ctx:PostgreSQLParser.CreatestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createstmt.
    def exitCreatestmt(self, ctx:PostgreSQLParser.CreatestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttemp.
    def enterOpttemp(self, ctx:PostgreSQLParser.OpttempContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttemp.
    def exitOpttemp(self, ctx:PostgreSQLParser.OpttempContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttableelementlist.
    def enterOpttableelementlist(self, ctx:PostgreSQLParser.OpttableelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttableelementlist.
    def exitOpttableelementlist(self, ctx:PostgreSQLParser.OpttableelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttypedtableelementlist.
    def enterOpttypedtableelementlist(self, ctx:PostgreSQLParser.OpttypedtableelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttypedtableelementlist.
    def exitOpttypedtableelementlist(self, ctx:PostgreSQLParser.OpttypedtableelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableelementlist.
    def enterTableelementlist(self, ctx:PostgreSQLParser.TableelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableelementlist.
    def exitTableelementlist(self, ctx:PostgreSQLParser.TableelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#typedtableelementlist.
    def enterTypedtableelementlist(self, ctx:PostgreSQLParser.TypedtableelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#typedtableelementlist.
    def exitTypedtableelementlist(self, ctx:PostgreSQLParser.TypedtableelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableelement.
    def enterTableelement(self, ctx:PostgreSQLParser.TableelementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableelement.
    def exitTableelement(self, ctx:PostgreSQLParser.TableelementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#typedtableelement.
    def enterTypedtableelement(self, ctx:PostgreSQLParser.TypedtableelementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#typedtableelement.
    def exitTypedtableelement(self, ctx:PostgreSQLParser.TypedtableelementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnDef.
    def enterColumnDef(self, ctx:PostgreSQLParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnDef.
    def exitColumnDef(self, ctx:PostgreSQLParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnOptions.
    def enterColumnOptions(self, ctx:PostgreSQLParser.ColumnOptionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnOptions.
    def exitColumnOptions(self, ctx:PostgreSQLParser.ColumnOptionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#colquallist.
    def enterColquallist(self, ctx:PostgreSQLParser.ColquallistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#colquallist.
    def exitColquallist(self, ctx:PostgreSQLParser.ColquallistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#colconstraint.
    def enterColconstraint(self, ctx:PostgreSQLParser.ColconstraintContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#colconstraint.
    def exitColconstraint(self, ctx:PostgreSQLParser.ColconstraintContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#colconstraintelem.
    def enterColconstraintelem(self, ctx:PostgreSQLParser.ColconstraintelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#colconstraintelem.
    def exitColconstraintelem(self, ctx:PostgreSQLParser.ColconstraintelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generated_when.
    def enterGenerated_when(self, ctx:PostgreSQLParser.Generated_whenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generated_when.
    def exitGenerated_when(self, ctx:PostgreSQLParser.Generated_whenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraintattr.
    def enterConstraintattr(self, ctx:PostgreSQLParser.ConstraintattrContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraintattr.
    def exitConstraintattr(self, ctx:PostgreSQLParser.ConstraintattrContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablelikeclause.
    def enterTablelikeclause(self, ctx:PostgreSQLParser.TablelikeclauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablelikeclause.
    def exitTablelikeclause(self, ctx:PostgreSQLParser.TablelikeclauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablelikeoptionlist.
    def enterTablelikeoptionlist(self, ctx:PostgreSQLParser.TablelikeoptionlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablelikeoptionlist.
    def exitTablelikeoptionlist(self, ctx:PostgreSQLParser.TablelikeoptionlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablelikeoption.
    def enterTablelikeoption(self, ctx:PostgreSQLParser.TablelikeoptionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablelikeoption.
    def exitTablelikeoption(self, ctx:PostgreSQLParser.TablelikeoptionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableconstraint.
    def enterTableconstraint(self, ctx:PostgreSQLParser.TableconstraintContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableconstraint.
    def exitTableconstraint(self, ctx:PostgreSQLParser.TableconstraintContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraintelem.
    def enterConstraintelem(self, ctx:PostgreSQLParser.ConstraintelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraintelem.
    def exitConstraintelem(self, ctx:PostgreSQLParser.ConstraintelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_no_inherit.
    def enterOpt_no_inherit(self, ctx:PostgreSQLParser.Opt_no_inheritContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_no_inherit.
    def exitOpt_no_inherit(self, ctx:PostgreSQLParser.Opt_no_inheritContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_column_list.
    def enterOpt_column_list(self, ctx:PostgreSQLParser.Opt_column_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_column_list.
    def exitOpt_column_list(self, ctx:PostgreSQLParser.Opt_column_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnlist.
    def enterColumnlist(self, ctx:PostgreSQLParser.ColumnlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnlist.
    def exitColumnlist(self, ctx:PostgreSQLParser.ColumnlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnElem.
    def enterColumnElem(self, ctx:PostgreSQLParser.ColumnElemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnElem.
    def exitColumnElem(self, ctx:PostgreSQLParser.ColumnElemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_c_include.
    def enterOpt_c_include(self, ctx:PostgreSQLParser.Opt_c_includeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_c_include.
    def exitOpt_c_include(self, ctx:PostgreSQLParser.Opt_c_includeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#key_match.
    def enterKey_match(self, ctx:PostgreSQLParser.Key_matchContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#key_match.
    def exitKey_match(self, ctx:PostgreSQLParser.Key_matchContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#exclusionconstraintlist.
    def enterExclusionconstraintlist(self, ctx:PostgreSQLParser.ExclusionconstraintlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#exclusionconstraintlist.
    def exitExclusionconstraintlist(self, ctx:PostgreSQLParser.ExclusionconstraintlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#exclusionconstraintelem.
    def enterExclusionconstraintelem(self, ctx:PostgreSQLParser.ExclusionconstraintelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#exclusionconstraintelem.
    def exitExclusionconstraintelem(self, ctx:PostgreSQLParser.ExclusionconstraintelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#exclusionwhereclause.
    def enterExclusionwhereclause(self, ctx:PostgreSQLParser.ExclusionwhereclauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#exclusionwhereclause.
    def exitExclusionwhereclause(self, ctx:PostgreSQLParser.ExclusionwhereclauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#key_actions.
    def enterKey_actions(self, ctx:PostgreSQLParser.Key_actionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#key_actions.
    def exitKey_actions(self, ctx:PostgreSQLParser.Key_actionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#key_update.
    def enterKey_update(self, ctx:PostgreSQLParser.Key_updateContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#key_update.
    def exitKey_update(self, ctx:PostgreSQLParser.Key_updateContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#key_delete.
    def enterKey_delete(self, ctx:PostgreSQLParser.Key_deleteContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#key_delete.
    def exitKey_delete(self, ctx:PostgreSQLParser.Key_deleteContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#key_action.
    def enterKey_action(self, ctx:PostgreSQLParser.Key_actionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#key_action.
    def exitKey_action(self, ctx:PostgreSQLParser.Key_actionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optinherit.
    def enterOptinherit(self, ctx:PostgreSQLParser.OptinheritContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optinherit.
    def exitOptinherit(self, ctx:PostgreSQLParser.OptinheritContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optpartitionspec.
    def enterOptpartitionspec(self, ctx:PostgreSQLParser.OptpartitionspecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optpartitionspec.
    def exitOptpartitionspec(self, ctx:PostgreSQLParser.OptpartitionspecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#partitionspec.
    def enterPartitionspec(self, ctx:PostgreSQLParser.PartitionspecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#partitionspec.
    def exitPartitionspec(self, ctx:PostgreSQLParser.PartitionspecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#part_params.
    def enterPart_params(self, ctx:PostgreSQLParser.Part_paramsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#part_params.
    def exitPart_params(self, ctx:PostgreSQLParser.Part_paramsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#part_elem.
    def enterPart_elem(self, ctx:PostgreSQLParser.Part_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#part_elem.
    def exitPart_elem(self, ctx:PostgreSQLParser.Part_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_access_method_clause.
    def enterTable_access_method_clause(self, ctx:PostgreSQLParser.Table_access_method_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_access_method_clause.
    def exitTable_access_method_clause(self, ctx:PostgreSQLParser.Table_access_method_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optwith.
    def enterOptwith(self, ctx:PostgreSQLParser.OptwithContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optwith.
    def exitOptwith(self, ctx:PostgreSQLParser.OptwithContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#oncommitoption.
    def enterOncommitoption(self, ctx:PostgreSQLParser.OncommitoptionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#oncommitoption.
    def exitOncommitoption(self, ctx:PostgreSQLParser.OncommitoptionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttablespace.
    def enterOpttablespace(self, ctx:PostgreSQLParser.OpttablespaceContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttablespace.
    def exitOpttablespace(self, ctx:PostgreSQLParser.OpttablespaceContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optconstablespace.
    def enterOptconstablespace(self, ctx:PostgreSQLParser.OptconstablespaceContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optconstablespace.
    def exitOptconstablespace(self, ctx:PostgreSQLParser.OptconstablespaceContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#existingindex.
    def enterExistingindex(self, ctx:PostgreSQLParser.ExistingindexContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#existingindex.
    def exitExistingindex(self, ctx:PostgreSQLParser.ExistingindexContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createstatsstmt.
    def enterCreatestatsstmt(self, ctx:PostgreSQLParser.CreatestatsstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createstatsstmt.
    def exitCreatestatsstmt(self, ctx:PostgreSQLParser.CreatestatsstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterstatsstmt.
    def enterAlterstatsstmt(self, ctx:PostgreSQLParser.AlterstatsstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterstatsstmt.
    def exitAlterstatsstmt(self, ctx:PostgreSQLParser.AlterstatsstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createasstmt.
    def enterCreateasstmt(self, ctx:PostgreSQLParser.CreateasstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createasstmt.
    def exitCreateasstmt(self, ctx:PostgreSQLParser.CreateasstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#create_as_target.
    def enterCreate_as_target(self, ctx:PostgreSQLParser.Create_as_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#create_as_target.
    def exitCreate_as_target(self, ctx:PostgreSQLParser.Create_as_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_with_data.
    def enterOpt_with_data(self, ctx:PostgreSQLParser.Opt_with_dataContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_with_data.
    def exitOpt_with_data(self, ctx:PostgreSQLParser.Opt_with_dataContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#creatematviewstmt.
    def enterCreatematviewstmt(self, ctx:PostgreSQLParser.CreatematviewstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#creatematviewstmt.
    def exitCreatematviewstmt(self, ctx:PostgreSQLParser.CreatematviewstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#create_mv_target.
    def enterCreate_mv_target(self, ctx:PostgreSQLParser.Create_mv_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#create_mv_target.
    def exitCreate_mv_target(self, ctx:PostgreSQLParser.Create_mv_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optnolog.
    def enterOptnolog(self, ctx:PostgreSQLParser.OptnologContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optnolog.
    def exitOptnolog(self, ctx:PostgreSQLParser.OptnologContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#refreshmatviewstmt.
    def enterRefreshmatviewstmt(self, ctx:PostgreSQLParser.RefreshmatviewstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#refreshmatviewstmt.
    def exitRefreshmatviewstmt(self, ctx:PostgreSQLParser.RefreshmatviewstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createseqstmt.
    def enterCreateseqstmt(self, ctx:PostgreSQLParser.CreateseqstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createseqstmt.
    def exitCreateseqstmt(self, ctx:PostgreSQLParser.CreateseqstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterseqstmt.
    def enterAlterseqstmt(self, ctx:PostgreSQLParser.AlterseqstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterseqstmt.
    def exitAlterseqstmt(self, ctx:PostgreSQLParser.AlterseqstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optseqoptlist.
    def enterOptseqoptlist(self, ctx:PostgreSQLParser.OptseqoptlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optseqoptlist.
    def exitOptseqoptlist(self, ctx:PostgreSQLParser.OptseqoptlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optparenthesizedseqoptlist.
    def enterOptparenthesizedseqoptlist(self, ctx:PostgreSQLParser.OptparenthesizedseqoptlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optparenthesizedseqoptlist.
    def exitOptparenthesizedseqoptlist(self, ctx:PostgreSQLParser.OptparenthesizedseqoptlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#seqoptlist.
    def enterSeqoptlist(self, ctx:PostgreSQLParser.SeqoptlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#seqoptlist.
    def exitSeqoptlist(self, ctx:PostgreSQLParser.SeqoptlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#seqoptelem.
    def enterSeqoptelem(self, ctx:PostgreSQLParser.SeqoptelemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#seqoptelem.
    def exitSeqoptelem(self, ctx:PostgreSQLParser.SeqoptelemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_by.
    def enterOpt_by(self, ctx:PostgreSQLParser.Opt_byContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_by.
    def exitOpt_by(self, ctx:PostgreSQLParser.Opt_byContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#numericonly.
    def enterNumericonly(self, ctx:PostgreSQLParser.NumericonlyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#numericonly.
    def exitNumericonly(self, ctx:PostgreSQLParser.NumericonlyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#numericonly_list.
    def enterNumericonly_list(self, ctx:PostgreSQLParser.Numericonly_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#numericonly_list.
    def exitNumericonly_list(self, ctx:PostgreSQLParser.Numericonly_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createplangstmt.
    def enterCreateplangstmt(self, ctx:PostgreSQLParser.CreateplangstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createplangstmt.
    def exitCreateplangstmt(self, ctx:PostgreSQLParser.CreateplangstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_trusted.
    def enterOpt_trusted(self, ctx:PostgreSQLParser.Opt_trustedContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_trusted.
    def exitOpt_trusted(self, ctx:PostgreSQLParser.Opt_trustedContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#handler_name.
    def enterHandler_name(self, ctx:PostgreSQLParser.Handler_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#handler_name.
    def exitHandler_name(self, ctx:PostgreSQLParser.Handler_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_inline_handler.
    def enterOpt_inline_handler(self, ctx:PostgreSQLParser.Opt_inline_handlerContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_inline_handler.
    def exitOpt_inline_handler(self, ctx:PostgreSQLParser.Opt_inline_handlerContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#validator_clause.
    def enterValidator_clause(self, ctx:PostgreSQLParser.Validator_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#validator_clause.
    def exitValidator_clause(self, ctx:PostgreSQLParser.Validator_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_validator.
    def enterOpt_validator(self, ctx:PostgreSQLParser.Opt_validatorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_validator.
    def exitOpt_validator(self, ctx:PostgreSQLParser.Opt_validatorContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_procedural.
    def enterOpt_procedural(self, ctx:PostgreSQLParser.Opt_proceduralContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_procedural.
    def exitOpt_procedural(self, ctx:PostgreSQLParser.Opt_proceduralContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createtablespacestmt.
    def enterCreatetablespacestmt(self, ctx:PostgreSQLParser.CreatetablespacestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createtablespacestmt.
    def exitCreatetablespacestmt(self, ctx:PostgreSQLParser.CreatetablespacestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttablespaceowner.
    def enterOpttablespaceowner(self, ctx:PostgreSQLParser.OpttablespaceownerContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttablespaceowner.
    def exitOpttablespaceowner(self, ctx:PostgreSQLParser.OpttablespaceownerContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#droptablespacestmt.
    def enterDroptablespacestmt(self, ctx:PostgreSQLParser.DroptablespacestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#droptablespacestmt.
    def exitDroptablespacestmt(self, ctx:PostgreSQLParser.DroptablespacestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createextensionstmt.
    def enterCreateextensionstmt(self, ctx:PostgreSQLParser.CreateextensionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createextensionstmt.
    def exitCreateextensionstmt(self, ctx:PostgreSQLParser.CreateextensionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#create_extension_opt_list.
    def enterCreate_extension_opt_list(self, ctx:PostgreSQLParser.Create_extension_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#create_extension_opt_list.
    def exitCreate_extension_opt_list(self, ctx:PostgreSQLParser.Create_extension_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#create_extension_opt_item.
    def enterCreate_extension_opt_item(self, ctx:PostgreSQLParser.Create_extension_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#create_extension_opt_item.
    def exitCreate_extension_opt_item(self, ctx:PostgreSQLParser.Create_extension_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterextensionstmt.
    def enterAlterextensionstmt(self, ctx:PostgreSQLParser.AlterextensionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterextensionstmt.
    def exitAlterextensionstmt(self, ctx:PostgreSQLParser.AlterextensionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_extension_opt_list.
    def enterAlter_extension_opt_list(self, ctx:PostgreSQLParser.Alter_extension_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_extension_opt_list.
    def exitAlter_extension_opt_list(self, ctx:PostgreSQLParser.Alter_extension_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_extension_opt_item.
    def enterAlter_extension_opt_item(self, ctx:PostgreSQLParser.Alter_extension_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_extension_opt_item.
    def exitAlter_extension_opt_item(self, ctx:PostgreSQLParser.Alter_extension_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterextensioncontentsstmt.
    def enterAlterextensioncontentsstmt(self, ctx:PostgreSQLParser.AlterextensioncontentsstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterextensioncontentsstmt.
    def exitAlterextensioncontentsstmt(self, ctx:PostgreSQLParser.AlterextensioncontentsstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createfdwstmt.
    def enterCreatefdwstmt(self, ctx:PostgreSQLParser.CreatefdwstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createfdwstmt.
    def exitCreatefdwstmt(self, ctx:PostgreSQLParser.CreatefdwstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#fdw_option.
    def enterFdw_option(self, ctx:PostgreSQLParser.Fdw_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#fdw_option.
    def exitFdw_option(self, ctx:PostgreSQLParser.Fdw_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#fdw_options.
    def enterFdw_options(self, ctx:PostgreSQLParser.Fdw_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#fdw_options.
    def exitFdw_options(self, ctx:PostgreSQLParser.Fdw_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_fdw_options.
    def enterOpt_fdw_options(self, ctx:PostgreSQLParser.Opt_fdw_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_fdw_options.
    def exitOpt_fdw_options(self, ctx:PostgreSQLParser.Opt_fdw_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterfdwstmt.
    def enterAlterfdwstmt(self, ctx:PostgreSQLParser.AlterfdwstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterfdwstmt.
    def exitAlterfdwstmt(self, ctx:PostgreSQLParser.AlterfdwstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#create_generic_options.
    def enterCreate_generic_options(self, ctx:PostgreSQLParser.Create_generic_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#create_generic_options.
    def exitCreate_generic_options(self, ctx:PostgreSQLParser.Create_generic_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_option_list.
    def enterGeneric_option_list(self, ctx:PostgreSQLParser.Generic_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_option_list.
    def exitGeneric_option_list(self, ctx:PostgreSQLParser.Generic_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_generic_options.
    def enterAlter_generic_options(self, ctx:PostgreSQLParser.Alter_generic_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_generic_options.
    def exitAlter_generic_options(self, ctx:PostgreSQLParser.Alter_generic_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_generic_option_list.
    def enterAlter_generic_option_list(self, ctx:PostgreSQLParser.Alter_generic_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_generic_option_list.
    def exitAlter_generic_option_list(self, ctx:PostgreSQLParser.Alter_generic_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alter_generic_option_elem.
    def enterAlter_generic_option_elem(self, ctx:PostgreSQLParser.Alter_generic_option_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alter_generic_option_elem.
    def exitAlter_generic_option_elem(self, ctx:PostgreSQLParser.Alter_generic_option_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_option_elem.
    def enterGeneric_option_elem(self, ctx:PostgreSQLParser.Generic_option_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_option_elem.
    def exitGeneric_option_elem(self, ctx:PostgreSQLParser.Generic_option_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_option_name.
    def enterGeneric_option_name(self, ctx:PostgreSQLParser.Generic_option_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_option_name.
    def exitGeneric_option_name(self, ctx:PostgreSQLParser.Generic_option_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generic_option_arg.
    def enterGeneric_option_arg(self, ctx:PostgreSQLParser.Generic_option_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generic_option_arg.
    def exitGeneric_option_arg(self, ctx:PostgreSQLParser.Generic_option_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createforeignserverstmt.
    def enterCreateforeignserverstmt(self, ctx:PostgreSQLParser.CreateforeignserverstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createforeignserverstmt.
    def exitCreateforeignserverstmt(self, ctx:PostgreSQLParser.CreateforeignserverstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_type.
    def enterOpt_type(self, ctx:PostgreSQLParser.Opt_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_type.
    def exitOpt_type(self, ctx:PostgreSQLParser.Opt_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#foreign_server_version.
    def enterForeign_server_version(self, ctx:PostgreSQLParser.Foreign_server_versionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#foreign_server_version.
    def exitForeign_server_version(self, ctx:PostgreSQLParser.Foreign_server_versionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_foreign_server_version.
    def enterOpt_foreign_server_version(self, ctx:PostgreSQLParser.Opt_foreign_server_versionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_foreign_server_version.
    def exitOpt_foreign_server_version(self, ctx:PostgreSQLParser.Opt_foreign_server_versionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterforeignserverstmt.
    def enterAlterforeignserverstmt(self, ctx:PostgreSQLParser.AlterforeignserverstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterforeignserverstmt.
    def exitAlterforeignserverstmt(self, ctx:PostgreSQLParser.AlterforeignserverstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createforeigntablestmt.
    def enterCreateforeigntablestmt(self, ctx:PostgreSQLParser.CreateforeigntablestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createforeigntablestmt.
    def exitCreateforeigntablestmt(self, ctx:PostgreSQLParser.CreateforeigntablestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#importforeignschemastmt.
    def enterImportforeignschemastmt(self, ctx:PostgreSQLParser.ImportforeignschemastmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#importforeignschemastmt.
    def exitImportforeignschemastmt(self, ctx:PostgreSQLParser.ImportforeignschemastmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#import_qualification_type.
    def enterImport_qualification_type(self, ctx:PostgreSQLParser.Import_qualification_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#import_qualification_type.
    def exitImport_qualification_type(self, ctx:PostgreSQLParser.Import_qualification_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#import_qualification.
    def enterImport_qualification(self, ctx:PostgreSQLParser.Import_qualificationContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#import_qualification.
    def exitImport_qualification(self, ctx:PostgreSQLParser.Import_qualificationContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createusermappingstmt.
    def enterCreateusermappingstmt(self, ctx:PostgreSQLParser.CreateusermappingstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createusermappingstmt.
    def exitCreateusermappingstmt(self, ctx:PostgreSQLParser.CreateusermappingstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#auth_ident.
    def enterAuth_ident(self, ctx:PostgreSQLParser.Auth_identContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#auth_ident.
    def exitAuth_ident(self, ctx:PostgreSQLParser.Auth_identContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropusermappingstmt.
    def enterDropusermappingstmt(self, ctx:PostgreSQLParser.DropusermappingstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropusermappingstmt.
    def exitDropusermappingstmt(self, ctx:PostgreSQLParser.DropusermappingstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterusermappingstmt.
    def enterAlterusermappingstmt(self, ctx:PostgreSQLParser.AlterusermappingstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterusermappingstmt.
    def exitAlterusermappingstmt(self, ctx:PostgreSQLParser.AlterusermappingstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createpolicystmt.
    def enterCreatepolicystmt(self, ctx:PostgreSQLParser.CreatepolicystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createpolicystmt.
    def exitCreatepolicystmt(self, ctx:PostgreSQLParser.CreatepolicystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterpolicystmt.
    def enterAlterpolicystmt(self, ctx:PostgreSQLParser.AlterpolicystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterpolicystmt.
    def exitAlterpolicystmt(self, ctx:PostgreSQLParser.AlterpolicystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecurityoptionalexpr.
    def enterRowsecurityoptionalexpr(self, ctx:PostgreSQLParser.RowsecurityoptionalexprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecurityoptionalexpr.
    def exitRowsecurityoptionalexpr(self, ctx:PostgreSQLParser.RowsecurityoptionalexprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecurityoptionalwithcheck.
    def enterRowsecurityoptionalwithcheck(self, ctx:PostgreSQLParser.RowsecurityoptionalwithcheckContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecurityoptionalwithcheck.
    def exitRowsecurityoptionalwithcheck(self, ctx:PostgreSQLParser.RowsecurityoptionalwithcheckContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecuritydefaulttorole.
    def enterRowsecuritydefaulttorole(self, ctx:PostgreSQLParser.RowsecuritydefaulttoroleContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecuritydefaulttorole.
    def exitRowsecuritydefaulttorole(self, ctx:PostgreSQLParser.RowsecuritydefaulttoroleContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecurityoptionaltorole.
    def enterRowsecurityoptionaltorole(self, ctx:PostgreSQLParser.RowsecurityoptionaltoroleContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecurityoptionaltorole.
    def exitRowsecurityoptionaltorole(self, ctx:PostgreSQLParser.RowsecurityoptionaltoroleContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecuritydefaultpermissive.
    def enterRowsecuritydefaultpermissive(self, ctx:PostgreSQLParser.RowsecuritydefaultpermissiveContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecuritydefaultpermissive.
    def exitRowsecuritydefaultpermissive(self, ctx:PostgreSQLParser.RowsecuritydefaultpermissiveContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsecuritydefaultforcmd.
    def enterRowsecuritydefaultforcmd(self, ctx:PostgreSQLParser.RowsecuritydefaultforcmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsecuritydefaultforcmd.
    def exitRowsecuritydefaultforcmd(self, ctx:PostgreSQLParser.RowsecuritydefaultforcmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#row_security_cmd.
    def enterRow_security_cmd(self, ctx:PostgreSQLParser.Row_security_cmdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#row_security_cmd.
    def exitRow_security_cmd(self, ctx:PostgreSQLParser.Row_security_cmdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createamstmt.
    def enterCreateamstmt(self, ctx:PostgreSQLParser.CreateamstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createamstmt.
    def exitCreateamstmt(self, ctx:PostgreSQLParser.CreateamstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#am_type.
    def enterAm_type(self, ctx:PostgreSQLParser.Am_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#am_type.
    def exitAm_type(self, ctx:PostgreSQLParser.Am_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createtrigstmt.
    def enterCreatetrigstmt(self, ctx:PostgreSQLParser.CreatetrigstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createtrigstmt.
    def exitCreatetrigstmt(self, ctx:PostgreSQLParser.CreatetrigstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggeractiontime.
    def enterTriggeractiontime(self, ctx:PostgreSQLParser.TriggeractiontimeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggeractiontime.
    def exitTriggeractiontime(self, ctx:PostgreSQLParser.TriggeractiontimeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerevents.
    def enterTriggerevents(self, ctx:PostgreSQLParser.TriggereventsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerevents.
    def exitTriggerevents(self, ctx:PostgreSQLParser.TriggereventsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggeroneevent.
    def enterTriggeroneevent(self, ctx:PostgreSQLParser.TriggeroneeventContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggeroneevent.
    def exitTriggeroneevent(self, ctx:PostgreSQLParser.TriggeroneeventContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerreferencing.
    def enterTriggerreferencing(self, ctx:PostgreSQLParser.TriggerreferencingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerreferencing.
    def exitTriggerreferencing(self, ctx:PostgreSQLParser.TriggerreferencingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggertransitions.
    def enterTriggertransitions(self, ctx:PostgreSQLParser.TriggertransitionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggertransitions.
    def exitTriggertransitions(self, ctx:PostgreSQLParser.TriggertransitionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggertransition.
    def enterTriggertransition(self, ctx:PostgreSQLParser.TriggertransitionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggertransition.
    def exitTriggertransition(self, ctx:PostgreSQLParser.TriggertransitionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transitionoldornew.
    def enterTransitionoldornew(self, ctx:PostgreSQLParser.TransitionoldornewContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transitionoldornew.
    def exitTransitionoldornew(self, ctx:PostgreSQLParser.TransitionoldornewContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transitionrowortable.
    def enterTransitionrowortable(self, ctx:PostgreSQLParser.TransitionrowortableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transitionrowortable.
    def exitTransitionrowortable(self, ctx:PostgreSQLParser.TransitionrowortableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transitionrelname.
    def enterTransitionrelname(self, ctx:PostgreSQLParser.TransitionrelnameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transitionrelname.
    def exitTransitionrelname(self, ctx:PostgreSQLParser.TransitionrelnameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerforspec.
    def enterTriggerforspec(self, ctx:PostgreSQLParser.TriggerforspecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerforspec.
    def exitTriggerforspec(self, ctx:PostgreSQLParser.TriggerforspecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerforopteach.
    def enterTriggerforopteach(self, ctx:PostgreSQLParser.TriggerforopteachContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerforopteach.
    def exitTriggerforopteach(self, ctx:PostgreSQLParser.TriggerforopteachContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerfortype.
    def enterTriggerfortype(self, ctx:PostgreSQLParser.TriggerfortypeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerfortype.
    def exitTriggerfortype(self, ctx:PostgreSQLParser.TriggerfortypeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerwhen.
    def enterTriggerwhen(self, ctx:PostgreSQLParser.TriggerwhenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerwhen.
    def exitTriggerwhen(self, ctx:PostgreSQLParser.TriggerwhenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#function_or_procedure.
    def enterFunction_or_procedure(self, ctx:PostgreSQLParser.Function_or_procedureContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#function_or_procedure.
    def exitFunction_or_procedure(self, ctx:PostgreSQLParser.Function_or_procedureContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerfuncargs.
    def enterTriggerfuncargs(self, ctx:PostgreSQLParser.TriggerfuncargsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerfuncargs.
    def exitTriggerfuncargs(self, ctx:PostgreSQLParser.TriggerfuncargsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#triggerfuncarg.
    def enterTriggerfuncarg(self, ctx:PostgreSQLParser.TriggerfuncargContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#triggerfuncarg.
    def exitTriggerfuncarg(self, ctx:PostgreSQLParser.TriggerfuncargContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#optconstrfromtable.
    def enterOptconstrfromtable(self, ctx:PostgreSQLParser.OptconstrfromtableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#optconstrfromtable.
    def exitOptconstrfromtable(self, ctx:PostgreSQLParser.OptconstrfromtableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraintattributespec.
    def enterConstraintattributespec(self, ctx:PostgreSQLParser.ConstraintattributespecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraintattributespec.
    def exitConstraintattributespec(self, ctx:PostgreSQLParser.ConstraintattributespecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constraintattributeElem.
    def enterConstraintattributeElem(self, ctx:PostgreSQLParser.ConstraintattributeElemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constraintattributeElem.
    def exitConstraintattributeElem(self, ctx:PostgreSQLParser.ConstraintattributeElemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createeventtrigstmt.
    def enterCreateeventtrigstmt(self, ctx:PostgreSQLParser.CreateeventtrigstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createeventtrigstmt.
    def exitCreateeventtrigstmt(self, ctx:PostgreSQLParser.CreateeventtrigstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#event_trigger_when_list.
    def enterEvent_trigger_when_list(self, ctx:PostgreSQLParser.Event_trigger_when_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#event_trigger_when_list.
    def exitEvent_trigger_when_list(self, ctx:PostgreSQLParser.Event_trigger_when_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#event_trigger_when_item.
    def enterEvent_trigger_when_item(self, ctx:PostgreSQLParser.Event_trigger_when_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#event_trigger_when_item.
    def exitEvent_trigger_when_item(self, ctx:PostgreSQLParser.Event_trigger_when_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#event_trigger_value_list.
    def enterEvent_trigger_value_list(self, ctx:PostgreSQLParser.Event_trigger_value_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#event_trigger_value_list.
    def exitEvent_trigger_value_list(self, ctx:PostgreSQLParser.Event_trigger_value_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altereventtrigstmt.
    def enterAltereventtrigstmt(self, ctx:PostgreSQLParser.AltereventtrigstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altereventtrigstmt.
    def exitAltereventtrigstmt(self, ctx:PostgreSQLParser.AltereventtrigstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#enable_trigger.
    def enterEnable_trigger(self, ctx:PostgreSQLParser.Enable_triggerContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#enable_trigger.
    def exitEnable_trigger(self, ctx:PostgreSQLParser.Enable_triggerContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createassertionstmt.
    def enterCreateassertionstmt(self, ctx:PostgreSQLParser.CreateassertionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createassertionstmt.
    def exitCreateassertionstmt(self, ctx:PostgreSQLParser.CreateassertionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#definestmt.
    def enterDefinestmt(self, ctx:PostgreSQLParser.DefinestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#definestmt.
    def exitDefinestmt(self, ctx:PostgreSQLParser.DefinestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#definition.
    def enterDefinition(self, ctx:PostgreSQLParser.DefinitionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#definition.
    def exitDefinition(self, ctx:PostgreSQLParser.DefinitionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#def_list.
    def enterDef_list(self, ctx:PostgreSQLParser.Def_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#def_list.
    def exitDef_list(self, ctx:PostgreSQLParser.Def_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#def_elem.
    def enterDef_elem(self, ctx:PostgreSQLParser.Def_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#def_elem.
    def exitDef_elem(self, ctx:PostgreSQLParser.Def_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#def_arg.
    def enterDef_arg(self, ctx:PostgreSQLParser.Def_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#def_arg.
    def exitDef_arg(self, ctx:PostgreSQLParser.Def_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#old_aggr_definition.
    def enterOld_aggr_definition(self, ctx:PostgreSQLParser.Old_aggr_definitionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#old_aggr_definition.
    def exitOld_aggr_definition(self, ctx:PostgreSQLParser.Old_aggr_definitionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#old_aggr_list.
    def enterOld_aggr_list(self, ctx:PostgreSQLParser.Old_aggr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#old_aggr_list.
    def exitOld_aggr_list(self, ctx:PostgreSQLParser.Old_aggr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#old_aggr_elem.
    def enterOld_aggr_elem(self, ctx:PostgreSQLParser.Old_aggr_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#old_aggr_elem.
    def exitOld_aggr_elem(self, ctx:PostgreSQLParser.Old_aggr_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_enum_val_list.
    def enterOpt_enum_val_list(self, ctx:PostgreSQLParser.Opt_enum_val_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_enum_val_list.
    def exitOpt_enum_val_list(self, ctx:PostgreSQLParser.Opt_enum_val_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#enum_val_list.
    def enterEnum_val_list(self, ctx:PostgreSQLParser.Enum_val_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#enum_val_list.
    def exitEnum_val_list(self, ctx:PostgreSQLParser.Enum_val_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterenumstmt.
    def enterAlterenumstmt(self, ctx:PostgreSQLParser.AlterenumstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterenumstmt.
    def exitAlterenumstmt(self, ctx:PostgreSQLParser.AlterenumstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_if_not_exists.
    def enterOpt_if_not_exists(self, ctx:PostgreSQLParser.Opt_if_not_existsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_if_not_exists.
    def exitOpt_if_not_exists(self, ctx:PostgreSQLParser.Opt_if_not_existsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createopclassstmt.
    def enterCreateopclassstmt(self, ctx:PostgreSQLParser.CreateopclassstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createopclassstmt.
    def exitCreateopclassstmt(self, ctx:PostgreSQLParser.CreateopclassstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opclass_item_list.
    def enterOpclass_item_list(self, ctx:PostgreSQLParser.Opclass_item_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opclass_item_list.
    def exitOpclass_item_list(self, ctx:PostgreSQLParser.Opclass_item_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opclass_item.
    def enterOpclass_item(self, ctx:PostgreSQLParser.Opclass_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opclass_item.
    def exitOpclass_item(self, ctx:PostgreSQLParser.Opclass_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_default.
    def enterOpt_default(self, ctx:PostgreSQLParser.Opt_defaultContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_default.
    def exitOpt_default(self, ctx:PostgreSQLParser.Opt_defaultContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_opfamily.
    def enterOpt_opfamily(self, ctx:PostgreSQLParser.Opt_opfamilyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_opfamily.
    def exitOpt_opfamily(self, ctx:PostgreSQLParser.Opt_opfamilyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opclass_purpose.
    def enterOpclass_purpose(self, ctx:PostgreSQLParser.Opclass_purposeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opclass_purpose.
    def exitOpclass_purpose(self, ctx:PostgreSQLParser.Opclass_purposeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_recheck.
    def enterOpt_recheck(self, ctx:PostgreSQLParser.Opt_recheckContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_recheck.
    def exitOpt_recheck(self, ctx:PostgreSQLParser.Opt_recheckContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createopfamilystmt.
    def enterCreateopfamilystmt(self, ctx:PostgreSQLParser.CreateopfamilystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createopfamilystmt.
    def exitCreateopfamilystmt(self, ctx:PostgreSQLParser.CreateopfamilystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alteropfamilystmt.
    def enterAlteropfamilystmt(self, ctx:PostgreSQLParser.AlteropfamilystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alteropfamilystmt.
    def exitAlteropfamilystmt(self, ctx:PostgreSQLParser.AlteropfamilystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opclass_drop_list.
    def enterOpclass_drop_list(self, ctx:PostgreSQLParser.Opclass_drop_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opclass_drop_list.
    def exitOpclass_drop_list(self, ctx:PostgreSQLParser.Opclass_drop_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opclass_drop.
    def enterOpclass_drop(self, ctx:PostgreSQLParser.Opclass_dropContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opclass_drop.
    def exitOpclass_drop(self, ctx:PostgreSQLParser.Opclass_dropContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropopclassstmt.
    def enterDropopclassstmt(self, ctx:PostgreSQLParser.DropopclassstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropopclassstmt.
    def exitDropopclassstmt(self, ctx:PostgreSQLParser.DropopclassstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropopfamilystmt.
    def enterDropopfamilystmt(self, ctx:PostgreSQLParser.DropopfamilystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropopfamilystmt.
    def exitDropopfamilystmt(self, ctx:PostgreSQLParser.DropopfamilystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropownedstmt.
    def enterDropownedstmt(self, ctx:PostgreSQLParser.DropownedstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropownedstmt.
    def exitDropownedstmt(self, ctx:PostgreSQLParser.DropownedstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reassignownedstmt.
    def enterReassignownedstmt(self, ctx:PostgreSQLParser.ReassignownedstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reassignownedstmt.
    def exitReassignownedstmt(self, ctx:PostgreSQLParser.ReassignownedstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropstmt.
    def enterDropstmt(self, ctx:PostgreSQLParser.DropstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropstmt.
    def exitDropstmt(self, ctx:PostgreSQLParser.DropstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#object_type_any_name.
    def enterObject_type_any_name(self, ctx:PostgreSQLParser.Object_type_any_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#object_type_any_name.
    def exitObject_type_any_name(self, ctx:PostgreSQLParser.Object_type_any_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#object_type_name.
    def enterObject_type_name(self, ctx:PostgreSQLParser.Object_type_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#object_type_name.
    def exitObject_type_name(self, ctx:PostgreSQLParser.Object_type_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#drop_type_name.
    def enterDrop_type_name(self, ctx:PostgreSQLParser.Drop_type_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#drop_type_name.
    def exitDrop_type_name(self, ctx:PostgreSQLParser.Drop_type_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#object_type_name_on_any_name.
    def enterObject_type_name_on_any_name(self, ctx:PostgreSQLParser.Object_type_name_on_any_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#object_type_name_on_any_name.
    def exitObject_type_name_on_any_name(self, ctx:PostgreSQLParser.Object_type_name_on_any_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#any_name_list.
    def enterAny_name_list(self, ctx:PostgreSQLParser.Any_name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#any_name_list.
    def exitAny_name_list(self, ctx:PostgreSQLParser.Any_name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#any_name.
    def enterAny_name(self, ctx:PostgreSQLParser.Any_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#any_name.
    def exitAny_name(self, ctx:PostgreSQLParser.Any_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#attrs.
    def enterAttrs(self, ctx:PostgreSQLParser.AttrsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#attrs.
    def exitAttrs(self, ctx:PostgreSQLParser.AttrsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#type_name_list.
    def enterType_name_list(self, ctx:PostgreSQLParser.Type_name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#type_name_list.
    def exitType_name_list(self, ctx:PostgreSQLParser.Type_name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#truncatestmt.
    def enterTruncatestmt(self, ctx:PostgreSQLParser.TruncatestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#truncatestmt.
    def exitTruncatestmt(self, ctx:PostgreSQLParser.TruncatestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_restart_seqs.
    def enterOpt_restart_seqs(self, ctx:PostgreSQLParser.Opt_restart_seqsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_restart_seqs.
    def exitOpt_restart_seqs(self, ctx:PostgreSQLParser.Opt_restart_seqsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#commentstmt.
    def enterCommentstmt(self, ctx:PostgreSQLParser.CommentstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#commentstmt.
    def exitCommentstmt(self, ctx:PostgreSQLParser.CommentstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#comment_text.
    def enterComment_text(self, ctx:PostgreSQLParser.Comment_textContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#comment_text.
    def exitComment_text(self, ctx:PostgreSQLParser.Comment_textContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#seclabelstmt.
    def enterSeclabelstmt(self, ctx:PostgreSQLParser.SeclabelstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#seclabelstmt.
    def exitSeclabelstmt(self, ctx:PostgreSQLParser.SeclabelstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_provider.
    def enterOpt_provider(self, ctx:PostgreSQLParser.Opt_providerContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_provider.
    def exitOpt_provider(self, ctx:PostgreSQLParser.Opt_providerContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#security_label.
    def enterSecurity_label(self, ctx:PostgreSQLParser.Security_labelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#security_label.
    def exitSecurity_label(self, ctx:PostgreSQLParser.Security_labelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#fetchstmt.
    def enterFetchstmt(self, ctx:PostgreSQLParser.FetchstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#fetchstmt.
    def exitFetchstmt(self, ctx:PostgreSQLParser.FetchstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#fetch_args.
    def enterFetch_args(self, ctx:PostgreSQLParser.Fetch_argsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#fetch_args.
    def exitFetch_args(self, ctx:PostgreSQLParser.Fetch_argsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#from_in.
    def enterFrom_in(self, ctx:PostgreSQLParser.From_inContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#from_in.
    def exitFrom_in(self, ctx:PostgreSQLParser.From_inContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_from_in.
    def enterOpt_from_in(self, ctx:PostgreSQLParser.Opt_from_inContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_from_in.
    def exitOpt_from_in(self, ctx:PostgreSQLParser.Opt_from_inContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#grantstmt.
    def enterGrantstmt(self, ctx:PostgreSQLParser.GrantstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#grantstmt.
    def exitGrantstmt(self, ctx:PostgreSQLParser.GrantstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#revokestmt.
    def enterRevokestmt(self, ctx:PostgreSQLParser.RevokestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#revokestmt.
    def exitRevokestmt(self, ctx:PostgreSQLParser.RevokestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#privileges.
    def enterPrivileges(self, ctx:PostgreSQLParser.PrivilegesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#privileges.
    def exitPrivileges(self, ctx:PostgreSQLParser.PrivilegesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#privilege_list.
    def enterPrivilege_list(self, ctx:PostgreSQLParser.Privilege_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#privilege_list.
    def exitPrivilege_list(self, ctx:PostgreSQLParser.Privilege_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#privilege.
    def enterPrivilege(self, ctx:PostgreSQLParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#privilege.
    def exitPrivilege(self, ctx:PostgreSQLParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#privilege_target.
    def enterPrivilege_target(self, ctx:PostgreSQLParser.Privilege_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#privilege_target.
    def exitPrivilege_target(self, ctx:PostgreSQLParser.Privilege_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#grantee_list.
    def enterGrantee_list(self, ctx:PostgreSQLParser.Grantee_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#grantee_list.
    def exitGrantee_list(self, ctx:PostgreSQLParser.Grantee_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#grantee.
    def enterGrantee(self, ctx:PostgreSQLParser.GranteeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#grantee.
    def exitGrantee(self, ctx:PostgreSQLParser.GranteeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_grant_grant_option.
    def enterOpt_grant_grant_option(self, ctx:PostgreSQLParser.Opt_grant_grant_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_grant_grant_option.
    def exitOpt_grant_grant_option(self, ctx:PostgreSQLParser.Opt_grant_grant_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#grantrolestmt.
    def enterGrantrolestmt(self, ctx:PostgreSQLParser.GrantrolestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#grantrolestmt.
    def exitGrantrolestmt(self, ctx:PostgreSQLParser.GrantrolestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#revokerolestmt.
    def enterRevokerolestmt(self, ctx:PostgreSQLParser.RevokerolestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#revokerolestmt.
    def exitRevokerolestmt(self, ctx:PostgreSQLParser.RevokerolestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_grant_admin_option.
    def enterOpt_grant_admin_option(self, ctx:PostgreSQLParser.Opt_grant_admin_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_grant_admin_option.
    def exitOpt_grant_admin_option(self, ctx:PostgreSQLParser.Opt_grant_admin_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_granted_by.
    def enterOpt_granted_by(self, ctx:PostgreSQLParser.Opt_granted_byContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_granted_by.
    def exitOpt_granted_by(self, ctx:PostgreSQLParser.Opt_granted_byContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterdefaultprivilegesstmt.
    def enterAlterdefaultprivilegesstmt(self, ctx:PostgreSQLParser.AlterdefaultprivilegesstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterdefaultprivilegesstmt.
    def exitAlterdefaultprivilegesstmt(self, ctx:PostgreSQLParser.AlterdefaultprivilegesstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#defacloptionlist.
    def enterDefacloptionlist(self, ctx:PostgreSQLParser.DefacloptionlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#defacloptionlist.
    def exitDefacloptionlist(self, ctx:PostgreSQLParser.DefacloptionlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#defacloption.
    def enterDefacloption(self, ctx:PostgreSQLParser.DefacloptionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#defacloption.
    def exitDefacloption(self, ctx:PostgreSQLParser.DefacloptionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#defaclaction.
    def enterDefaclaction(self, ctx:PostgreSQLParser.DefaclactionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#defaclaction.
    def exitDefaclaction(self, ctx:PostgreSQLParser.DefaclactionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#defacl_privilege_target.
    def enterDefacl_privilege_target(self, ctx:PostgreSQLParser.Defacl_privilege_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#defacl_privilege_target.
    def exitDefacl_privilege_target(self, ctx:PostgreSQLParser.Defacl_privilege_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#indexstmt.
    def enterIndexstmt(self, ctx:PostgreSQLParser.IndexstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#indexstmt.
    def exitIndexstmt(self, ctx:PostgreSQLParser.IndexstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_unique.
    def enterOpt_unique(self, ctx:PostgreSQLParser.Opt_uniqueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_unique.
    def exitOpt_unique(self, ctx:PostgreSQLParser.Opt_uniqueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_concurrently.
    def enterOpt_concurrently(self, ctx:PostgreSQLParser.Opt_concurrentlyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_concurrently.
    def exitOpt_concurrently(self, ctx:PostgreSQLParser.Opt_concurrentlyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_index_name.
    def enterOpt_index_name(self, ctx:PostgreSQLParser.Opt_index_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_index_name.
    def exitOpt_index_name(self, ctx:PostgreSQLParser.Opt_index_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#access_method_clause.
    def enterAccess_method_clause(self, ctx:PostgreSQLParser.Access_method_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#access_method_clause.
    def exitAccess_method_clause(self, ctx:PostgreSQLParser.Access_method_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#index_params.
    def enterIndex_params(self, ctx:PostgreSQLParser.Index_paramsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#index_params.
    def exitIndex_params(self, ctx:PostgreSQLParser.Index_paramsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#index_elem_options.
    def enterIndex_elem_options(self, ctx:PostgreSQLParser.Index_elem_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#index_elem_options.
    def exitIndex_elem_options(self, ctx:PostgreSQLParser.Index_elem_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#index_elem.
    def enterIndex_elem(self, ctx:PostgreSQLParser.Index_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#index_elem.
    def exitIndex_elem(self, ctx:PostgreSQLParser.Index_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_include.
    def enterOpt_include(self, ctx:PostgreSQLParser.Opt_includeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_include.
    def exitOpt_include(self, ctx:PostgreSQLParser.Opt_includeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#index_including_params.
    def enterIndex_including_params(self, ctx:PostgreSQLParser.Index_including_paramsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#index_including_params.
    def exitIndex_including_params(self, ctx:PostgreSQLParser.Index_including_paramsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_collate.
    def enterOpt_collate(self, ctx:PostgreSQLParser.Opt_collateContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_collate.
    def exitOpt_collate(self, ctx:PostgreSQLParser.Opt_collateContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_class.
    def enterOpt_class(self, ctx:PostgreSQLParser.Opt_classContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_class.
    def exitOpt_class(self, ctx:PostgreSQLParser.Opt_classContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_asc_desc.
    def enterOpt_asc_desc(self, ctx:PostgreSQLParser.Opt_asc_descContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_asc_desc.
    def exitOpt_asc_desc(self, ctx:PostgreSQLParser.Opt_asc_descContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_nulls_order.
    def enterOpt_nulls_order(self, ctx:PostgreSQLParser.Opt_nulls_orderContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_nulls_order.
    def exitOpt_nulls_order(self, ctx:PostgreSQLParser.Opt_nulls_orderContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createfunctionstmt.
    def enterCreatefunctionstmt(self, ctx:PostgreSQLParser.CreatefunctionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createfunctionstmt.
    def exitCreatefunctionstmt(self, ctx:PostgreSQLParser.CreatefunctionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_or_replace.
    def enterOpt_or_replace(self, ctx:PostgreSQLParser.Opt_or_replaceContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_or_replace.
    def exitOpt_or_replace(self, ctx:PostgreSQLParser.Opt_or_replaceContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_args.
    def enterFunc_args(self, ctx:PostgreSQLParser.Func_argsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_args.
    def exitFunc_args(self, ctx:PostgreSQLParser.Func_argsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_args_list.
    def enterFunc_args_list(self, ctx:PostgreSQLParser.Func_args_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_args_list.
    def exitFunc_args_list(self, ctx:PostgreSQLParser.Func_args_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#function_with_argtypes_list.
    def enterFunction_with_argtypes_list(self, ctx:PostgreSQLParser.Function_with_argtypes_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#function_with_argtypes_list.
    def exitFunction_with_argtypes_list(self, ctx:PostgreSQLParser.Function_with_argtypes_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#function_with_argtypes.
    def enterFunction_with_argtypes(self, ctx:PostgreSQLParser.Function_with_argtypesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#function_with_argtypes.
    def exitFunction_with_argtypes(self, ctx:PostgreSQLParser.Function_with_argtypesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_args_with_defaults.
    def enterFunc_args_with_defaults(self, ctx:PostgreSQLParser.Func_args_with_defaultsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_args_with_defaults.
    def exitFunc_args_with_defaults(self, ctx:PostgreSQLParser.Func_args_with_defaultsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_args_with_defaults_list.
    def enterFunc_args_with_defaults_list(self, ctx:PostgreSQLParser.Func_args_with_defaults_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_args_with_defaults_list.
    def exitFunc_args_with_defaults_list(self, ctx:PostgreSQLParser.Func_args_with_defaults_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_arg.
    def enterFunc_arg(self, ctx:PostgreSQLParser.Func_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_arg.
    def exitFunc_arg(self, ctx:PostgreSQLParser.Func_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#arg_class.
    def enterArg_class(self, ctx:PostgreSQLParser.Arg_classContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#arg_class.
    def exitArg_class(self, ctx:PostgreSQLParser.Arg_classContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#param_name.
    def enterParam_name(self, ctx:PostgreSQLParser.Param_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#param_name.
    def exitParam_name(self, ctx:PostgreSQLParser.Param_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_return.
    def enterFunc_return(self, ctx:PostgreSQLParser.Func_returnContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_return.
    def exitFunc_return(self, ctx:PostgreSQLParser.Func_returnContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_type.
    def enterFunc_type(self, ctx:PostgreSQLParser.Func_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_type.
    def exitFunc_type(self, ctx:PostgreSQLParser.Func_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_arg_with_default.
    def enterFunc_arg_with_default(self, ctx:PostgreSQLParser.Func_arg_with_defaultContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_arg_with_default.
    def exitFunc_arg_with_default(self, ctx:PostgreSQLParser.Func_arg_with_defaultContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggr_arg.
    def enterAggr_arg(self, ctx:PostgreSQLParser.Aggr_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggr_arg.
    def exitAggr_arg(self, ctx:PostgreSQLParser.Aggr_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggr_args.
    def enterAggr_args(self, ctx:PostgreSQLParser.Aggr_argsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggr_args.
    def exitAggr_args(self, ctx:PostgreSQLParser.Aggr_argsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggr_args_list.
    def enterAggr_args_list(self, ctx:PostgreSQLParser.Aggr_args_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggr_args_list.
    def exitAggr_args_list(self, ctx:PostgreSQLParser.Aggr_args_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggregate_with_argtypes.
    def enterAggregate_with_argtypes(self, ctx:PostgreSQLParser.Aggregate_with_argtypesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggregate_with_argtypes.
    def exitAggregate_with_argtypes(self, ctx:PostgreSQLParser.Aggregate_with_argtypesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggregate_with_argtypes_list.
    def enterAggregate_with_argtypes_list(self, ctx:PostgreSQLParser.Aggregate_with_argtypes_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggregate_with_argtypes_list.
    def exitAggregate_with_argtypes_list(self, ctx:PostgreSQLParser.Aggregate_with_argtypes_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createfunc_opt_list.
    def enterCreatefunc_opt_list(self, ctx:PostgreSQLParser.Createfunc_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createfunc_opt_list.
    def exitCreatefunc_opt_list(self, ctx:PostgreSQLParser.Createfunc_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#common_func_opt_item.
    def enterCommon_func_opt_item(self, ctx:PostgreSQLParser.Common_func_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#common_func_opt_item.
    def exitCommon_func_opt_item(self, ctx:PostgreSQLParser.Common_func_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createfunc_opt_item.
    def enterCreatefunc_opt_item(self, ctx:PostgreSQLParser.Createfunc_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createfunc_opt_item.
    def exitCreatefunc_opt_item(self, ctx:PostgreSQLParser.Createfunc_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_as.
    def enterFunc_as(self, ctx:PostgreSQLParser.Func_asContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_as.
    def exitFunc_as(self, ctx:PostgreSQLParser.Func_asContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transform_type_list.
    def enterTransform_type_list(self, ctx:PostgreSQLParser.Transform_type_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transform_type_list.
    def exitTransform_type_list(self, ctx:PostgreSQLParser.Transform_type_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_definition.
    def enterOpt_definition(self, ctx:PostgreSQLParser.Opt_definitionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_definition.
    def exitOpt_definition(self, ctx:PostgreSQLParser.Opt_definitionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_func_column.
    def enterTable_func_column(self, ctx:PostgreSQLParser.Table_func_columnContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_func_column.
    def exitTable_func_column(self, ctx:PostgreSQLParser.Table_func_columnContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_func_column_list.
    def enterTable_func_column_list(self, ctx:PostgreSQLParser.Table_func_column_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_func_column_list.
    def exitTable_func_column_list(self, ctx:PostgreSQLParser.Table_func_column_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterfunctionstmt.
    def enterAlterfunctionstmt(self, ctx:PostgreSQLParser.AlterfunctionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterfunctionstmt.
    def exitAlterfunctionstmt(self, ctx:PostgreSQLParser.AlterfunctionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterfunc_opt_list.
    def enterAlterfunc_opt_list(self, ctx:PostgreSQLParser.Alterfunc_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterfunc_opt_list.
    def exitAlterfunc_opt_list(self, ctx:PostgreSQLParser.Alterfunc_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_restrict.
    def enterOpt_restrict(self, ctx:PostgreSQLParser.Opt_restrictContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_restrict.
    def exitOpt_restrict(self, ctx:PostgreSQLParser.Opt_restrictContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#removefuncstmt.
    def enterRemovefuncstmt(self, ctx:PostgreSQLParser.RemovefuncstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#removefuncstmt.
    def exitRemovefuncstmt(self, ctx:PostgreSQLParser.RemovefuncstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#removeaggrstmt.
    def enterRemoveaggrstmt(self, ctx:PostgreSQLParser.RemoveaggrstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#removeaggrstmt.
    def exitRemoveaggrstmt(self, ctx:PostgreSQLParser.RemoveaggrstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#removeoperstmt.
    def enterRemoveoperstmt(self, ctx:PostgreSQLParser.RemoveoperstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#removeoperstmt.
    def exitRemoveoperstmt(self, ctx:PostgreSQLParser.RemoveoperstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#oper_argtypes.
    def enterOper_argtypes(self, ctx:PostgreSQLParser.Oper_argtypesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#oper_argtypes.
    def exitOper_argtypes(self, ctx:PostgreSQLParser.Oper_argtypesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#any_operator.
    def enterAny_operator(self, ctx:PostgreSQLParser.Any_operatorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#any_operator.
    def exitAny_operator(self, ctx:PostgreSQLParser.Any_operatorContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#operator_with_argtypes_list.
    def enterOperator_with_argtypes_list(self, ctx:PostgreSQLParser.Operator_with_argtypes_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#operator_with_argtypes_list.
    def exitOperator_with_argtypes_list(self, ctx:PostgreSQLParser.Operator_with_argtypes_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#operator_with_argtypes.
    def enterOperator_with_argtypes(self, ctx:PostgreSQLParser.Operator_with_argtypesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#operator_with_argtypes.
    def exitOperator_with_argtypes(self, ctx:PostgreSQLParser.Operator_with_argtypesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dostmt.
    def enterDostmt(self, ctx:PostgreSQLParser.DostmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dostmt.
    def exitDostmt(self, ctx:PostgreSQLParser.DostmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dostmt_opt_list.
    def enterDostmt_opt_list(self, ctx:PostgreSQLParser.Dostmt_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dostmt_opt_list.
    def exitDostmt_opt_list(self, ctx:PostgreSQLParser.Dostmt_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dostmt_opt_item.
    def enterDostmt_opt_item(self, ctx:PostgreSQLParser.Dostmt_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dostmt_opt_item.
    def exitDostmt_opt_item(self, ctx:PostgreSQLParser.Dostmt_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createcaststmt.
    def enterCreatecaststmt(self, ctx:PostgreSQLParser.CreatecaststmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createcaststmt.
    def exitCreatecaststmt(self, ctx:PostgreSQLParser.CreatecaststmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cast_context.
    def enterCast_context(self, ctx:PostgreSQLParser.Cast_contextContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cast_context.
    def exitCast_context(self, ctx:PostgreSQLParser.Cast_contextContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropcaststmt.
    def enterDropcaststmt(self, ctx:PostgreSQLParser.DropcaststmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropcaststmt.
    def exitDropcaststmt(self, ctx:PostgreSQLParser.DropcaststmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_if_exists.
    def enterOpt_if_exists(self, ctx:PostgreSQLParser.Opt_if_existsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_if_exists.
    def exitOpt_if_exists(self, ctx:PostgreSQLParser.Opt_if_existsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createtransformstmt.
    def enterCreatetransformstmt(self, ctx:PostgreSQLParser.CreatetransformstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createtransformstmt.
    def exitCreatetransformstmt(self, ctx:PostgreSQLParser.CreatetransformstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transform_element_list.
    def enterTransform_element_list(self, ctx:PostgreSQLParser.Transform_element_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transform_element_list.
    def exitTransform_element_list(self, ctx:PostgreSQLParser.Transform_element_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#droptransformstmt.
    def enterDroptransformstmt(self, ctx:PostgreSQLParser.DroptransformstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#droptransformstmt.
    def exitDroptransformstmt(self, ctx:PostgreSQLParser.DroptransformstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reindexstmt.
    def enterReindexstmt(self, ctx:PostgreSQLParser.ReindexstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reindexstmt.
    def exitReindexstmt(self, ctx:PostgreSQLParser.ReindexstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reindex_target_type.
    def enterReindex_target_type(self, ctx:PostgreSQLParser.Reindex_target_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reindex_target_type.
    def exitReindex_target_type(self, ctx:PostgreSQLParser.Reindex_target_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reindex_target_multitable.
    def enterReindex_target_multitable(self, ctx:PostgreSQLParser.Reindex_target_multitableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reindex_target_multitable.
    def exitReindex_target_multitable(self, ctx:PostgreSQLParser.Reindex_target_multitableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reindex_option_list.
    def enterReindex_option_list(self, ctx:PostgreSQLParser.Reindex_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reindex_option_list.
    def exitReindex_option_list(self, ctx:PostgreSQLParser.Reindex_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reindex_option_elem.
    def enterReindex_option_elem(self, ctx:PostgreSQLParser.Reindex_option_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reindex_option_elem.
    def exitReindex_option_elem(self, ctx:PostgreSQLParser.Reindex_option_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altertblspcstmt.
    def enterAltertblspcstmt(self, ctx:PostgreSQLParser.AltertblspcstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altertblspcstmt.
    def exitAltertblspcstmt(self, ctx:PostgreSQLParser.AltertblspcstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#renamestmt.
    def enterRenamestmt(self, ctx:PostgreSQLParser.RenamestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#renamestmt.
    def exitRenamestmt(self, ctx:PostgreSQLParser.RenamestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_column.
    def enterOpt_column(self, ctx:PostgreSQLParser.Opt_columnContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_column.
    def exitOpt_column(self, ctx:PostgreSQLParser.Opt_columnContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_set_data.
    def enterOpt_set_data(self, ctx:PostgreSQLParser.Opt_set_dataContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_set_data.
    def exitOpt_set_data(self, ctx:PostgreSQLParser.Opt_set_dataContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterobjectdependsstmt.
    def enterAlterobjectdependsstmt(self, ctx:PostgreSQLParser.AlterobjectdependsstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterobjectdependsstmt.
    def exitAlterobjectdependsstmt(self, ctx:PostgreSQLParser.AlterobjectdependsstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_no.
    def enterOpt_no(self, ctx:PostgreSQLParser.Opt_noContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_no.
    def exitOpt_no(self, ctx:PostgreSQLParser.Opt_noContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterobjectschemastmt.
    def enterAlterobjectschemastmt(self, ctx:PostgreSQLParser.AlterobjectschemastmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterobjectschemastmt.
    def exitAlterobjectschemastmt(self, ctx:PostgreSQLParser.AlterobjectschemastmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alteroperatorstmt.
    def enterAlteroperatorstmt(self, ctx:PostgreSQLParser.AlteroperatorstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alteroperatorstmt.
    def exitAlteroperatorstmt(self, ctx:PostgreSQLParser.AlteroperatorstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#operator_def_list.
    def enterOperator_def_list(self, ctx:PostgreSQLParser.Operator_def_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#operator_def_list.
    def exitOperator_def_list(self, ctx:PostgreSQLParser.Operator_def_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#operator_def_elem.
    def enterOperator_def_elem(self, ctx:PostgreSQLParser.Operator_def_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#operator_def_elem.
    def exitOperator_def_elem(self, ctx:PostgreSQLParser.Operator_def_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#operator_def_arg.
    def enterOperator_def_arg(self, ctx:PostgreSQLParser.Operator_def_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#operator_def_arg.
    def exitOperator_def_arg(self, ctx:PostgreSQLParser.Operator_def_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altertypestmt.
    def enterAltertypestmt(self, ctx:PostgreSQLParser.AltertypestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altertypestmt.
    def exitAltertypestmt(self, ctx:PostgreSQLParser.AltertypestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterownerstmt.
    def enterAlterownerstmt(self, ctx:PostgreSQLParser.AlterownerstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterownerstmt.
    def exitAlterownerstmt(self, ctx:PostgreSQLParser.AlterownerstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createpublicationstmt.
    def enterCreatepublicationstmt(self, ctx:PostgreSQLParser.CreatepublicationstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createpublicationstmt.
    def exitCreatepublicationstmt(self, ctx:PostgreSQLParser.CreatepublicationstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_publication_for_tables.
    def enterOpt_publication_for_tables(self, ctx:PostgreSQLParser.Opt_publication_for_tablesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_publication_for_tables.
    def exitOpt_publication_for_tables(self, ctx:PostgreSQLParser.Opt_publication_for_tablesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#publication_for_tables.
    def enterPublication_for_tables(self, ctx:PostgreSQLParser.Publication_for_tablesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#publication_for_tables.
    def exitPublication_for_tables(self, ctx:PostgreSQLParser.Publication_for_tablesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterpublicationstmt.
    def enterAlterpublicationstmt(self, ctx:PostgreSQLParser.AlterpublicationstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterpublicationstmt.
    def exitAlterpublicationstmt(self, ctx:PostgreSQLParser.AlterpublicationstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createsubscriptionstmt.
    def enterCreatesubscriptionstmt(self, ctx:PostgreSQLParser.CreatesubscriptionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createsubscriptionstmt.
    def exitCreatesubscriptionstmt(self, ctx:PostgreSQLParser.CreatesubscriptionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#publication_name_list.
    def enterPublication_name_list(self, ctx:PostgreSQLParser.Publication_name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#publication_name_list.
    def exitPublication_name_list(self, ctx:PostgreSQLParser.Publication_name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#publication_name_item.
    def enterPublication_name_item(self, ctx:PostgreSQLParser.Publication_name_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#publication_name_item.
    def exitPublication_name_item(self, ctx:PostgreSQLParser.Publication_name_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altersubscriptionstmt.
    def enterAltersubscriptionstmt(self, ctx:PostgreSQLParser.AltersubscriptionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altersubscriptionstmt.
    def exitAltersubscriptionstmt(self, ctx:PostgreSQLParser.AltersubscriptionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropsubscriptionstmt.
    def enterDropsubscriptionstmt(self, ctx:PostgreSQLParser.DropsubscriptionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropsubscriptionstmt.
    def exitDropsubscriptionstmt(self, ctx:PostgreSQLParser.DropsubscriptionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rulestmt.
    def enterRulestmt(self, ctx:PostgreSQLParser.RulestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rulestmt.
    def exitRulestmt(self, ctx:PostgreSQLParser.RulestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#ruleactionlist.
    def enterRuleactionlist(self, ctx:PostgreSQLParser.RuleactionlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#ruleactionlist.
    def exitRuleactionlist(self, ctx:PostgreSQLParser.RuleactionlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#ruleactionmulti.
    def enterRuleactionmulti(self, ctx:PostgreSQLParser.RuleactionmultiContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#ruleactionmulti.
    def exitRuleactionmulti(self, ctx:PostgreSQLParser.RuleactionmultiContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#ruleactionstmt.
    def enterRuleactionstmt(self, ctx:PostgreSQLParser.RuleactionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#ruleactionstmt.
    def exitRuleactionstmt(self, ctx:PostgreSQLParser.RuleactionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#ruleactionstmtOrEmpty.
    def enterRuleactionstmtOrEmpty(self, ctx:PostgreSQLParser.RuleactionstmtOrEmptyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#ruleactionstmtOrEmpty.
    def exitRuleactionstmtOrEmpty(self, ctx:PostgreSQLParser.RuleactionstmtOrEmptyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#event.
    def enterEvent(self, ctx:PostgreSQLParser.EventContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#event.
    def exitEvent(self, ctx:PostgreSQLParser.EventContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_instead.
    def enterOpt_instead(self, ctx:PostgreSQLParser.Opt_insteadContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_instead.
    def exitOpt_instead(self, ctx:PostgreSQLParser.Opt_insteadContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#notifystmt.
    def enterNotifystmt(self, ctx:PostgreSQLParser.NotifystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#notifystmt.
    def exitNotifystmt(self, ctx:PostgreSQLParser.NotifystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#notify_payload.
    def enterNotify_payload(self, ctx:PostgreSQLParser.Notify_payloadContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#notify_payload.
    def exitNotify_payload(self, ctx:PostgreSQLParser.Notify_payloadContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#listenstmt.
    def enterListenstmt(self, ctx:PostgreSQLParser.ListenstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#listenstmt.
    def exitListenstmt(self, ctx:PostgreSQLParser.ListenstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#unlistenstmt.
    def enterUnlistenstmt(self, ctx:PostgreSQLParser.UnlistenstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#unlistenstmt.
    def exitUnlistenstmt(self, ctx:PostgreSQLParser.UnlistenstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transactionstmt.
    def enterTransactionstmt(self, ctx:PostgreSQLParser.TransactionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transactionstmt.
    def exitTransactionstmt(self, ctx:PostgreSQLParser.TransactionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_transaction.
    def enterOpt_transaction(self, ctx:PostgreSQLParser.Opt_transactionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_transaction.
    def exitOpt_transaction(self, ctx:PostgreSQLParser.Opt_transactionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transaction_mode_item.
    def enterTransaction_mode_item(self, ctx:PostgreSQLParser.Transaction_mode_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transaction_mode_item.
    def exitTransaction_mode_item(self, ctx:PostgreSQLParser.Transaction_mode_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transaction_mode_list.
    def enterTransaction_mode_list(self, ctx:PostgreSQLParser.Transaction_mode_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transaction_mode_list.
    def exitTransaction_mode_list(self, ctx:PostgreSQLParser.Transaction_mode_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#transaction_mode_list_or_empty.
    def enterTransaction_mode_list_or_empty(self, ctx:PostgreSQLParser.Transaction_mode_list_or_emptyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#transaction_mode_list_or_empty.
    def exitTransaction_mode_list_or_empty(self, ctx:PostgreSQLParser.Transaction_mode_list_or_emptyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_transaction_chain.
    def enterOpt_transaction_chain(self, ctx:PostgreSQLParser.Opt_transaction_chainContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_transaction_chain.
    def exitOpt_transaction_chain(self, ctx:PostgreSQLParser.Opt_transaction_chainContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#viewstmt.
    def enterViewstmt(self, ctx:PostgreSQLParser.ViewstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#viewstmt.
    def exitViewstmt(self, ctx:PostgreSQLParser.ViewstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_check_option.
    def enterOpt_check_option(self, ctx:PostgreSQLParser.Opt_check_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_check_option.
    def exitOpt_check_option(self, ctx:PostgreSQLParser.Opt_check_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#loadstmt.
    def enterLoadstmt(self, ctx:PostgreSQLParser.LoadstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#loadstmt.
    def exitLoadstmt(self, ctx:PostgreSQLParser.LoadstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdbstmt.
    def enterCreatedbstmt(self, ctx:PostgreSQLParser.CreatedbstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdbstmt.
    def exitCreatedbstmt(self, ctx:PostgreSQLParser.CreatedbstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdb_opt_list.
    def enterCreatedb_opt_list(self, ctx:PostgreSQLParser.Createdb_opt_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdb_opt_list.
    def exitCreatedb_opt_list(self, ctx:PostgreSQLParser.Createdb_opt_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdb_opt_items.
    def enterCreatedb_opt_items(self, ctx:PostgreSQLParser.Createdb_opt_itemsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdb_opt_items.
    def exitCreatedb_opt_items(self, ctx:PostgreSQLParser.Createdb_opt_itemsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdb_opt_item.
    def enterCreatedb_opt_item(self, ctx:PostgreSQLParser.Createdb_opt_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdb_opt_item.
    def exitCreatedb_opt_item(self, ctx:PostgreSQLParser.Createdb_opt_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdb_opt_name.
    def enterCreatedb_opt_name(self, ctx:PostgreSQLParser.Createdb_opt_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdb_opt_name.
    def exitCreatedb_opt_name(self, ctx:PostgreSQLParser.Createdb_opt_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_equal.
    def enterOpt_equal(self, ctx:PostgreSQLParser.Opt_equalContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_equal.
    def exitOpt_equal(self, ctx:PostgreSQLParser.Opt_equalContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterdatabasestmt.
    def enterAlterdatabasestmt(self, ctx:PostgreSQLParser.AlterdatabasestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterdatabasestmt.
    def exitAlterdatabasestmt(self, ctx:PostgreSQLParser.AlterdatabasestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterdatabasesetstmt.
    def enterAlterdatabasesetstmt(self, ctx:PostgreSQLParser.AlterdatabasesetstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterdatabasesetstmt.
    def exitAlterdatabasesetstmt(self, ctx:PostgreSQLParser.AlterdatabasesetstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropdbstmt.
    def enterDropdbstmt(self, ctx:PostgreSQLParser.DropdbstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropdbstmt.
    def exitDropdbstmt(self, ctx:PostgreSQLParser.DropdbstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#drop_option_list.
    def enterDrop_option_list(self, ctx:PostgreSQLParser.Drop_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#drop_option_list.
    def exitDrop_option_list(self, ctx:PostgreSQLParser.Drop_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#drop_option.
    def enterDrop_option(self, ctx:PostgreSQLParser.Drop_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#drop_option.
    def exitDrop_option(self, ctx:PostgreSQLParser.Drop_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altercollationstmt.
    def enterAltercollationstmt(self, ctx:PostgreSQLParser.AltercollationstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altercollationstmt.
    def exitAltercollationstmt(self, ctx:PostgreSQLParser.AltercollationstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altersystemstmt.
    def enterAltersystemstmt(self, ctx:PostgreSQLParser.AltersystemstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altersystemstmt.
    def exitAltersystemstmt(self, ctx:PostgreSQLParser.AltersystemstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createdomainstmt.
    def enterCreatedomainstmt(self, ctx:PostgreSQLParser.CreatedomainstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createdomainstmt.
    def exitCreatedomainstmt(self, ctx:PostgreSQLParser.CreatedomainstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterdomainstmt.
    def enterAlterdomainstmt(self, ctx:PostgreSQLParser.AlterdomainstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterdomainstmt.
    def exitAlterdomainstmt(self, ctx:PostgreSQLParser.AlterdomainstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_as.
    def enterOpt_as(self, ctx:PostgreSQLParser.Opt_asContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_as.
    def exitOpt_as(self, ctx:PostgreSQLParser.Opt_asContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altertsdictionarystmt.
    def enterAltertsdictionarystmt(self, ctx:PostgreSQLParser.AltertsdictionarystmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altertsdictionarystmt.
    def exitAltertsdictionarystmt(self, ctx:PostgreSQLParser.AltertsdictionarystmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#altertsconfigurationstmt.
    def enterAltertsconfigurationstmt(self, ctx:PostgreSQLParser.AltertsconfigurationstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#altertsconfigurationstmt.
    def exitAltertsconfigurationstmt(self, ctx:PostgreSQLParser.AltertsconfigurationstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#any_with.
    def enterAny_with(self, ctx:PostgreSQLParser.Any_withContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#any_with.
    def exitAny_with(self, ctx:PostgreSQLParser.Any_withContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#createconversionstmt.
    def enterCreateconversionstmt(self, ctx:PostgreSQLParser.CreateconversionstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createconversionstmt.
    def exitCreateconversionstmt(self, ctx:PostgreSQLParser.CreateconversionstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#clusterstmt.
    def enterClusterstmt(self, ctx:PostgreSQLParser.ClusterstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#clusterstmt.
    def exitClusterstmt(self, ctx:PostgreSQLParser.ClusterstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cluster_index_specification.
    def enterCluster_index_specification(self, ctx:PostgreSQLParser.Cluster_index_specificationContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cluster_index_specification.
    def exitCluster_index_specification(self, ctx:PostgreSQLParser.Cluster_index_specificationContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vacuumstmt.
    def enterVacuumstmt(self, ctx:PostgreSQLParser.VacuumstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vacuumstmt.
    def exitVacuumstmt(self, ctx:PostgreSQLParser.VacuumstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#analyzestmt.
    def enterAnalyzestmt(self, ctx:PostgreSQLParser.AnalyzestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#analyzestmt.
    def exitAnalyzestmt(self, ctx:PostgreSQLParser.AnalyzestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vac_analyze_option_list.
    def enterVac_analyze_option_list(self, ctx:PostgreSQLParser.Vac_analyze_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vac_analyze_option_list.
    def exitVac_analyze_option_list(self, ctx:PostgreSQLParser.Vac_analyze_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#analyze_keyword.
    def enterAnalyze_keyword(self, ctx:PostgreSQLParser.Analyze_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#analyze_keyword.
    def exitAnalyze_keyword(self, ctx:PostgreSQLParser.Analyze_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vac_analyze_option_elem.
    def enterVac_analyze_option_elem(self, ctx:PostgreSQLParser.Vac_analyze_option_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vac_analyze_option_elem.
    def exitVac_analyze_option_elem(self, ctx:PostgreSQLParser.Vac_analyze_option_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vac_analyze_option_name.
    def enterVac_analyze_option_name(self, ctx:PostgreSQLParser.Vac_analyze_option_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vac_analyze_option_name.
    def exitVac_analyze_option_name(self, ctx:PostgreSQLParser.Vac_analyze_option_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vac_analyze_option_arg.
    def enterVac_analyze_option_arg(self, ctx:PostgreSQLParser.Vac_analyze_option_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vac_analyze_option_arg.
    def exitVac_analyze_option_arg(self, ctx:PostgreSQLParser.Vac_analyze_option_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_analyze.
    def enterOpt_analyze(self, ctx:PostgreSQLParser.Opt_analyzeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_analyze.
    def exitOpt_analyze(self, ctx:PostgreSQLParser.Opt_analyzeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_verbose.
    def enterOpt_verbose(self, ctx:PostgreSQLParser.Opt_verboseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_verbose.
    def exitOpt_verbose(self, ctx:PostgreSQLParser.Opt_verboseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_full.
    def enterOpt_full(self, ctx:PostgreSQLParser.Opt_fullContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_full.
    def exitOpt_full(self, ctx:PostgreSQLParser.Opt_fullContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_freeze.
    def enterOpt_freeze(self, ctx:PostgreSQLParser.Opt_freezeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_freeze.
    def exitOpt_freeze(self, ctx:PostgreSQLParser.Opt_freezeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_name_list.
    def enterOpt_name_list(self, ctx:PostgreSQLParser.Opt_name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_name_list.
    def exitOpt_name_list(self, ctx:PostgreSQLParser.Opt_name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vacuum_relation.
    def enterVacuum_relation(self, ctx:PostgreSQLParser.Vacuum_relationContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vacuum_relation.
    def exitVacuum_relation(self, ctx:PostgreSQLParser.Vacuum_relationContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#vacuum_relation_list.
    def enterVacuum_relation_list(self, ctx:PostgreSQLParser.Vacuum_relation_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#vacuum_relation_list.
    def exitVacuum_relation_list(self, ctx:PostgreSQLParser.Vacuum_relation_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_vacuum_relation_list.
    def enterOpt_vacuum_relation_list(self, ctx:PostgreSQLParser.Opt_vacuum_relation_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_vacuum_relation_list.
    def exitOpt_vacuum_relation_list(self, ctx:PostgreSQLParser.Opt_vacuum_relation_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explainstmt.
    def enterExplainstmt(self, ctx:PostgreSQLParser.ExplainstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explainstmt.
    def exitExplainstmt(self, ctx:PostgreSQLParser.ExplainstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explainablestmt.
    def enterExplainablestmt(self, ctx:PostgreSQLParser.ExplainablestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explainablestmt.
    def exitExplainablestmt(self, ctx:PostgreSQLParser.ExplainablestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explain_option_list.
    def enterExplain_option_list(self, ctx:PostgreSQLParser.Explain_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explain_option_list.
    def exitExplain_option_list(self, ctx:PostgreSQLParser.Explain_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explain_option_elem.
    def enterExplain_option_elem(self, ctx:PostgreSQLParser.Explain_option_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explain_option_elem.
    def exitExplain_option_elem(self, ctx:PostgreSQLParser.Explain_option_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explain_option_name.
    def enterExplain_option_name(self, ctx:PostgreSQLParser.Explain_option_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explain_option_name.
    def exitExplain_option_name(self, ctx:PostgreSQLParser.Explain_option_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explain_option_arg.
    def enterExplain_option_arg(self, ctx:PostgreSQLParser.Explain_option_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explain_option_arg.
    def exitExplain_option_arg(self, ctx:PostgreSQLParser.Explain_option_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#preparestmt.
    def enterPreparestmt(self, ctx:PostgreSQLParser.PreparestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#preparestmt.
    def exitPreparestmt(self, ctx:PostgreSQLParser.PreparestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#prep_type_clause.
    def enterPrep_type_clause(self, ctx:PostgreSQLParser.Prep_type_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#prep_type_clause.
    def exitPrep_type_clause(self, ctx:PostgreSQLParser.Prep_type_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#preparablestmt.
    def enterPreparablestmt(self, ctx:PostgreSQLParser.PreparablestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#preparablestmt.
    def exitPreparablestmt(self, ctx:PostgreSQLParser.PreparablestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#executestmt.
    def enterExecutestmt(self, ctx:PostgreSQLParser.ExecutestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#executestmt.
    def exitExecutestmt(self, ctx:PostgreSQLParser.ExecutestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#execute_param_clause.
    def enterExecute_param_clause(self, ctx:PostgreSQLParser.Execute_param_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#execute_param_clause.
    def exitExecute_param_clause(self, ctx:PostgreSQLParser.Execute_param_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#deallocatestmt.
    def enterDeallocatestmt(self, ctx:PostgreSQLParser.DeallocatestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#deallocatestmt.
    def exitDeallocatestmt(self, ctx:PostgreSQLParser.DeallocatestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insertstmt.
    def enterInsertstmt(self, ctx:PostgreSQLParser.InsertstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insertstmt.
    def exitInsertstmt(self, ctx:PostgreSQLParser.InsertstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insert_target.
    def enterInsert_target(self, ctx:PostgreSQLParser.Insert_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insert_target.
    def exitInsert_target(self, ctx:PostgreSQLParser.Insert_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insert_rest.
    def enterInsert_rest(self, ctx:PostgreSQLParser.Insert_restContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insert_rest.
    def exitInsert_rest(self, ctx:PostgreSQLParser.Insert_restContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#override_kind.
    def enterOverride_kind(self, ctx:PostgreSQLParser.Override_kindContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#override_kind.
    def exitOverride_kind(self, ctx:PostgreSQLParser.Override_kindContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insert_column_list.
    def enterInsert_column_list(self, ctx:PostgreSQLParser.Insert_column_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insert_column_list.
    def exitInsert_column_list(self, ctx:PostgreSQLParser.Insert_column_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insert_column_item.
    def enterInsert_column_item(self, ctx:PostgreSQLParser.Insert_column_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insert_column_item.
    def exitInsert_column_item(self, ctx:PostgreSQLParser.Insert_column_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_on_conflict.
    def enterOpt_on_conflict(self, ctx:PostgreSQLParser.Opt_on_conflictContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_on_conflict.
    def exitOpt_on_conflict(self, ctx:PostgreSQLParser.Opt_on_conflictContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_conf_expr.
    def enterOpt_conf_expr(self, ctx:PostgreSQLParser.Opt_conf_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_conf_expr.
    def exitOpt_conf_expr(self, ctx:PostgreSQLParser.Opt_conf_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#returning_clause.
    def enterReturning_clause(self, ctx:PostgreSQLParser.Returning_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#returning_clause.
    def exitReturning_clause(self, ctx:PostgreSQLParser.Returning_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#mergestmt.
    def enterMergestmt(self, ctx:PostgreSQLParser.MergestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#mergestmt.
    def exitMergestmt(self, ctx:PostgreSQLParser.MergestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#merge_insert_clause.
    def enterMerge_insert_clause(self, ctx:PostgreSQLParser.Merge_insert_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#merge_insert_clause.
    def exitMerge_insert_clause(self, ctx:PostgreSQLParser.Merge_insert_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#merge_update_clause.
    def enterMerge_update_clause(self, ctx:PostgreSQLParser.Merge_update_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#merge_update_clause.
    def exitMerge_update_clause(self, ctx:PostgreSQLParser.Merge_update_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#merge_delete_clause.
    def enterMerge_delete_clause(self, ctx:PostgreSQLParser.Merge_delete_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#merge_delete_clause.
    def exitMerge_delete_clause(self, ctx:PostgreSQLParser.Merge_delete_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#deletestmt.
    def enterDeletestmt(self, ctx:PostgreSQLParser.DeletestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#deletestmt.
    def exitDeletestmt(self, ctx:PostgreSQLParser.DeletestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#using_clause.
    def enterUsing_clause(self, ctx:PostgreSQLParser.Using_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#using_clause.
    def exitUsing_clause(self, ctx:PostgreSQLParser.Using_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#lockstmt.
    def enterLockstmt(self, ctx:PostgreSQLParser.LockstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#lockstmt.
    def exitLockstmt(self, ctx:PostgreSQLParser.LockstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_lock.
    def enterOpt_lock(self, ctx:PostgreSQLParser.Opt_lockContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_lock.
    def exitOpt_lock(self, ctx:PostgreSQLParser.Opt_lockContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#lock_type.
    def enterLock_type(self, ctx:PostgreSQLParser.Lock_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#lock_type.
    def exitLock_type(self, ctx:PostgreSQLParser.Lock_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_nowait.
    def enterOpt_nowait(self, ctx:PostgreSQLParser.Opt_nowaitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_nowait.
    def exitOpt_nowait(self, ctx:PostgreSQLParser.Opt_nowaitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_nowait_or_skip.
    def enterOpt_nowait_or_skip(self, ctx:PostgreSQLParser.Opt_nowait_or_skipContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_nowait_or_skip.
    def exitOpt_nowait_or_skip(self, ctx:PostgreSQLParser.Opt_nowait_or_skipContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#updatestmt.
    def enterUpdatestmt(self, ctx:PostgreSQLParser.UpdatestmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#updatestmt.
    def exitUpdatestmt(self, ctx:PostgreSQLParser.UpdatestmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_clause_list.
    def enterSet_clause_list(self, ctx:PostgreSQLParser.Set_clause_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_clause_list.
    def exitSet_clause_list(self, ctx:PostgreSQLParser.Set_clause_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_clause.
    def enterSet_clause(self, ctx:PostgreSQLParser.Set_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_clause.
    def exitSet_clause(self, ctx:PostgreSQLParser.Set_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_target.
    def enterSet_target(self, ctx:PostgreSQLParser.Set_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_target.
    def exitSet_target(self, ctx:PostgreSQLParser.Set_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#set_target_list.
    def enterSet_target_list(self, ctx:PostgreSQLParser.Set_target_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#set_target_list.
    def exitSet_target_list(self, ctx:PostgreSQLParser.Set_target_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#declarecursorstmt.
    def enterDeclarecursorstmt(self, ctx:PostgreSQLParser.DeclarecursorstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#declarecursorstmt.
    def exitDeclarecursorstmt(self, ctx:PostgreSQLParser.DeclarecursorstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cursor_name.
    def enterCursor_name(self, ctx:PostgreSQLParser.Cursor_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cursor_name.
    def exitCursor_name(self, ctx:PostgreSQLParser.Cursor_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cursor_options.
    def enterCursor_options(self, ctx:PostgreSQLParser.Cursor_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cursor_options.
    def exitCursor_options(self, ctx:PostgreSQLParser.Cursor_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_hold.
    def enterOpt_hold(self, ctx:PostgreSQLParser.Opt_holdContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_hold.
    def exitOpt_hold(self, ctx:PostgreSQLParser.Opt_holdContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#selectstmt.
    def enterSelectstmt(self, ctx:PostgreSQLParser.SelectstmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#selectstmt.
    def exitSelectstmt(self, ctx:PostgreSQLParser.SelectstmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_with_parens.
    def enterSelect_with_parens(self, ctx:PostgreSQLParser.Select_with_parensContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_with_parens.
    def exitSelect_with_parens(self, ctx:PostgreSQLParser.Select_with_parensContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_no_parens.
    def enterSelect_no_parens(self, ctx:PostgreSQLParser.Select_no_parensContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_no_parens.
    def exitSelect_no_parens(self, ctx:PostgreSQLParser.Select_no_parensContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_clause.
    def enterSelect_clause(self, ctx:PostgreSQLParser.Select_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_clause.
    def exitSelect_clause(self, ctx:PostgreSQLParser.Select_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#simple_select_intersect.
    def enterSimple_select_intersect(self, ctx:PostgreSQLParser.Simple_select_intersectContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#simple_select_intersect.
    def exitSimple_select_intersect(self, ctx:PostgreSQLParser.Simple_select_intersectContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#simple_select_pramary.
    def enterSimple_select_pramary(self, ctx:PostgreSQLParser.Simple_select_pramaryContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#simple_select_pramary.
    def exitSimple_select_pramary(self, ctx:PostgreSQLParser.Simple_select_pramaryContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#with_clause.
    def enterWith_clause(self, ctx:PostgreSQLParser.With_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#with_clause.
    def exitWith_clause(self, ctx:PostgreSQLParser.With_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cte_list.
    def enterCte_list(self, ctx:PostgreSQLParser.Cte_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cte_list.
    def exitCte_list(self, ctx:PostgreSQLParser.Cte_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#common_table_expr.
    def enterCommon_table_expr(self, ctx:PostgreSQLParser.Common_table_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#common_table_expr.
    def exitCommon_table_expr(self, ctx:PostgreSQLParser.Common_table_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_materialized.
    def enterOpt_materialized(self, ctx:PostgreSQLParser.Opt_materializedContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_materialized.
    def exitOpt_materialized(self, ctx:PostgreSQLParser.Opt_materializedContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_with_clause.
    def enterOpt_with_clause(self, ctx:PostgreSQLParser.Opt_with_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_with_clause.
    def exitOpt_with_clause(self, ctx:PostgreSQLParser.Opt_with_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#into_clause.
    def enterInto_clause(self, ctx:PostgreSQLParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#into_clause.
    def exitInto_clause(self, ctx:PostgreSQLParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_strict.
    def enterOpt_strict(self, ctx:PostgreSQLParser.Opt_strictContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_strict.
    def exitOpt_strict(self, ctx:PostgreSQLParser.Opt_strictContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttempTableName.
    def enterOpttempTableName(self, ctx:PostgreSQLParser.OpttempTableNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttempTableName.
    def exitOpttempTableName(self, ctx:PostgreSQLParser.OpttempTableNameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_table.
    def enterOpt_table(self, ctx:PostgreSQLParser.Opt_tableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_table.
    def exitOpt_table(self, ctx:PostgreSQLParser.Opt_tableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#all_or_distinct.
    def enterAll_or_distinct(self, ctx:PostgreSQLParser.All_or_distinctContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#all_or_distinct.
    def exitAll_or_distinct(self, ctx:PostgreSQLParser.All_or_distinctContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#distinct_clause.
    def enterDistinct_clause(self, ctx:PostgreSQLParser.Distinct_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#distinct_clause.
    def exitDistinct_clause(self, ctx:PostgreSQLParser.Distinct_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_all_clause.
    def enterOpt_all_clause(self, ctx:PostgreSQLParser.Opt_all_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_all_clause.
    def exitOpt_all_clause(self, ctx:PostgreSQLParser.Opt_all_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_sort_clause.
    def enterOpt_sort_clause(self, ctx:PostgreSQLParser.Opt_sort_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_sort_clause.
    def exitOpt_sort_clause(self, ctx:PostgreSQLParser.Opt_sort_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sort_clause.
    def enterSort_clause(self, ctx:PostgreSQLParser.Sort_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sort_clause.
    def exitSort_clause(self, ctx:PostgreSQLParser.Sort_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sortby_list.
    def enterSortby_list(self, ctx:PostgreSQLParser.Sortby_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sortby_list.
    def exitSortby_list(self, ctx:PostgreSQLParser.Sortby_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sortby.
    def enterSortby(self, ctx:PostgreSQLParser.SortbyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sortby.
    def exitSortby(self, ctx:PostgreSQLParser.SortbyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_limit.
    def enterSelect_limit(self, ctx:PostgreSQLParser.Select_limitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_limit.
    def exitSelect_limit(self, ctx:PostgreSQLParser.Select_limitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_select_limit.
    def enterOpt_select_limit(self, ctx:PostgreSQLParser.Opt_select_limitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_select_limit.
    def exitOpt_select_limit(self, ctx:PostgreSQLParser.Opt_select_limitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#limit_clause.
    def enterLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#limit_clause.
    def exitLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#offset_clause.
    def enterOffset_clause(self, ctx:PostgreSQLParser.Offset_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#offset_clause.
    def exitOffset_clause(self, ctx:PostgreSQLParser.Offset_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_limit_value.
    def enterSelect_limit_value(self, ctx:PostgreSQLParser.Select_limit_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_limit_value.
    def exitSelect_limit_value(self, ctx:PostgreSQLParser.Select_limit_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_offset_value.
    def enterSelect_offset_value(self, ctx:PostgreSQLParser.Select_offset_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_offset_value.
    def exitSelect_offset_value(self, ctx:PostgreSQLParser.Select_offset_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_fetch_first_value.
    def enterSelect_fetch_first_value(self, ctx:PostgreSQLParser.Select_fetch_first_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_fetch_first_value.
    def exitSelect_fetch_first_value(self, ctx:PostgreSQLParser.Select_fetch_first_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#i_or_f_const.
    def enterI_or_f_const(self, ctx:PostgreSQLParser.I_or_f_constContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#i_or_f_const.
    def exitI_or_f_const(self, ctx:PostgreSQLParser.I_or_f_constContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#row_or_rows.
    def enterRow_or_rows(self, ctx:PostgreSQLParser.Row_or_rowsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#row_or_rows.
    def exitRow_or_rows(self, ctx:PostgreSQLParser.Row_or_rowsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#first_or_next.
    def enterFirst_or_next(self, ctx:PostgreSQLParser.First_or_nextContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#first_or_next.
    def exitFirst_or_next(self, ctx:PostgreSQLParser.First_or_nextContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#group_clause.
    def enterGroup_clause(self, ctx:PostgreSQLParser.Group_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#group_clause.
    def exitGroup_clause(self, ctx:PostgreSQLParser.Group_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#group_by_list.
    def enterGroup_by_list(self, ctx:PostgreSQLParser.Group_by_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#group_by_list.
    def exitGroup_by_list(self, ctx:PostgreSQLParser.Group_by_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#group_by_item.
    def enterGroup_by_item(self, ctx:PostgreSQLParser.Group_by_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#group_by_item.
    def exitGroup_by_item(self, ctx:PostgreSQLParser.Group_by_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#empty_grouping_set.
    def enterEmpty_grouping_set(self, ctx:PostgreSQLParser.Empty_grouping_setContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#empty_grouping_set.
    def exitEmpty_grouping_set(self, ctx:PostgreSQLParser.Empty_grouping_setContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rollup_clause.
    def enterRollup_clause(self, ctx:PostgreSQLParser.Rollup_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rollup_clause.
    def exitRollup_clause(self, ctx:PostgreSQLParser.Rollup_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cube_clause.
    def enterCube_clause(self, ctx:PostgreSQLParser.Cube_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cube_clause.
    def exitCube_clause(self, ctx:PostgreSQLParser.Cube_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#grouping_sets_clause.
    def enterGrouping_sets_clause(self, ctx:PostgreSQLParser.Grouping_sets_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#grouping_sets_clause.
    def exitGrouping_sets_clause(self, ctx:PostgreSQLParser.Grouping_sets_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#having_clause.
    def enterHaving_clause(self, ctx:PostgreSQLParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#having_clause.
    def exitHaving_clause(self, ctx:PostgreSQLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_locking_clause.
    def enterFor_locking_clause(self, ctx:PostgreSQLParser.For_locking_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_locking_clause.
    def exitFor_locking_clause(self, ctx:PostgreSQLParser.For_locking_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_for_locking_clause.
    def enterOpt_for_locking_clause(self, ctx:PostgreSQLParser.Opt_for_locking_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_for_locking_clause.
    def exitOpt_for_locking_clause(self, ctx:PostgreSQLParser.Opt_for_locking_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_locking_items.
    def enterFor_locking_items(self, ctx:PostgreSQLParser.For_locking_itemsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_locking_items.
    def exitFor_locking_items(self, ctx:PostgreSQLParser.For_locking_itemsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_locking_item.
    def enterFor_locking_item(self, ctx:PostgreSQLParser.For_locking_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_locking_item.
    def exitFor_locking_item(self, ctx:PostgreSQLParser.For_locking_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_locking_strength.
    def enterFor_locking_strength(self, ctx:PostgreSQLParser.For_locking_strengthContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_locking_strength.
    def exitFor_locking_strength(self, ctx:PostgreSQLParser.For_locking_strengthContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#locked_rels_list.
    def enterLocked_rels_list(self, ctx:PostgreSQLParser.Locked_rels_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#locked_rels_list.
    def exitLocked_rels_list(self, ctx:PostgreSQLParser.Locked_rels_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#values_clause.
    def enterValues_clause(self, ctx:PostgreSQLParser.Values_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#values_clause.
    def exitValues_clause(self, ctx:PostgreSQLParser.Values_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#from_clause.
    def enterFrom_clause(self, ctx:PostgreSQLParser.From_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#from_clause.
    def exitFrom_clause(self, ctx:PostgreSQLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#from_list.
    def enterFrom_list(self, ctx:PostgreSQLParser.From_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#from_list.
    def exitFrom_list(self, ctx:PostgreSQLParser.From_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#non_ansi_join.
    def enterNon_ansi_join(self, ctx:PostgreSQLParser.Non_ansi_joinContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#non_ansi_join.
    def exitNon_ansi_join(self, ctx:PostgreSQLParser.Non_ansi_joinContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_ref.
    def enterTable_ref(self, ctx:PostgreSQLParser.Table_refContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_ref.
    def exitTable_ref(self, ctx:PostgreSQLParser.Table_refContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alias_clause.
    def enterAlias_clause(self, ctx:PostgreSQLParser.Alias_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alias_clause.
    def exitAlias_clause(self, ctx:PostgreSQLParser.Alias_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_alias_clause.
    def enterOpt_alias_clause(self, ctx:PostgreSQLParser.Opt_alias_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_alias_clause.
    def exitOpt_alias_clause(self, ctx:PostgreSQLParser.Opt_alias_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_alias_clause.
    def enterTable_alias_clause(self, ctx:PostgreSQLParser.Table_alias_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_alias_clause.
    def exitTable_alias_clause(self, ctx:PostgreSQLParser.Table_alias_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_alias_clause.
    def enterFunc_alias_clause(self, ctx:PostgreSQLParser.Func_alias_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_alias_clause.
    def exitFunc_alias_clause(self, ctx:PostgreSQLParser.Func_alias_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#join_type.
    def enterJoin_type(self, ctx:PostgreSQLParser.Join_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#join_type.
    def exitJoin_type(self, ctx:PostgreSQLParser.Join_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#join_qual.
    def enterJoin_qual(self, ctx:PostgreSQLParser.Join_qualContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#join_qual.
    def exitJoin_qual(self, ctx:PostgreSQLParser.Join_qualContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#relation_expr.
    def enterRelation_expr(self, ctx:PostgreSQLParser.Relation_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#relation_expr.
    def exitRelation_expr(self, ctx:PostgreSQLParser.Relation_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#relation_expr_list.
    def enterRelation_expr_list(self, ctx:PostgreSQLParser.Relation_expr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#relation_expr_list.
    def exitRelation_expr_list(self, ctx:PostgreSQLParser.Relation_expr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#relation_expr_opt_alias.
    def enterRelation_expr_opt_alias(self, ctx:PostgreSQLParser.Relation_expr_opt_aliasContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#relation_expr_opt_alias.
    def exitRelation_expr_opt_alias(self, ctx:PostgreSQLParser.Relation_expr_opt_aliasContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablesample_clause.
    def enterTablesample_clause(self, ctx:PostgreSQLParser.Tablesample_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablesample_clause.
    def exitTablesample_clause(self, ctx:PostgreSQLParser.Tablesample_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_repeatable_clause.
    def enterOpt_repeatable_clause(self, ctx:PostgreSQLParser.Opt_repeatable_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_repeatable_clause.
    def exitOpt_repeatable_clause(self, ctx:PostgreSQLParser.Opt_repeatable_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_table.
    def enterFunc_table(self, ctx:PostgreSQLParser.Func_tableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_table.
    def exitFunc_table(self, ctx:PostgreSQLParser.Func_tableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsfrom_item.
    def enterRowsfrom_item(self, ctx:PostgreSQLParser.Rowsfrom_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsfrom_item.
    def exitRowsfrom_item(self, ctx:PostgreSQLParser.Rowsfrom_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rowsfrom_list.
    def enterRowsfrom_list(self, ctx:PostgreSQLParser.Rowsfrom_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rowsfrom_list.
    def exitRowsfrom_list(self, ctx:PostgreSQLParser.Rowsfrom_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_col_def_list.
    def enterOpt_col_def_list(self, ctx:PostgreSQLParser.Opt_col_def_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_col_def_list.
    def exitOpt_col_def_list(self, ctx:PostgreSQLParser.Opt_col_def_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_ordinality.
    def enterOpt_ordinality(self, ctx:PostgreSQLParser.Opt_ordinalityContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_ordinality.
    def exitOpt_ordinality(self, ctx:PostgreSQLParser.Opt_ordinalityContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#where_clause.
    def enterWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#where_clause.
    def exitWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#where_or_current_clause.
    def enterWhere_or_current_clause(self, ctx:PostgreSQLParser.Where_or_current_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#where_or_current_clause.
    def exitWhere_or_current_clause(self, ctx:PostgreSQLParser.Where_or_current_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opttablefuncelementlist.
    def enterOpttablefuncelementlist(self, ctx:PostgreSQLParser.OpttablefuncelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opttablefuncelementlist.
    def exitOpttablefuncelementlist(self, ctx:PostgreSQLParser.OpttablefuncelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablefuncelementlist.
    def enterTablefuncelementlist(self, ctx:PostgreSQLParser.TablefuncelementlistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablefuncelementlist.
    def exitTablefuncelementlist(self, ctx:PostgreSQLParser.TablefuncelementlistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tablefuncelement.
    def enterTablefuncelement(self, ctx:PostgreSQLParser.TablefuncelementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tablefuncelement.
    def exitTablefuncelement(self, ctx:PostgreSQLParser.TablefuncelementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmltable.
    def enterXmltable(self, ctx:PostgreSQLParser.XmltableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmltable.
    def exitXmltable(self, ctx:PostgreSQLParser.XmltableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmltable_column_list.
    def enterXmltable_column_list(self, ctx:PostgreSQLParser.Xmltable_column_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmltable_column_list.
    def exitXmltable_column_list(self, ctx:PostgreSQLParser.Xmltable_column_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmltable_column_el.
    def enterXmltable_column_el(self, ctx:PostgreSQLParser.Xmltable_column_elContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmltable_column_el.
    def exitXmltable_column_el(self, ctx:PostgreSQLParser.Xmltable_column_elContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmltable_column_option_list.
    def enterXmltable_column_option_list(self, ctx:PostgreSQLParser.Xmltable_column_option_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmltable_column_option_list.
    def exitXmltable_column_option_list(self, ctx:PostgreSQLParser.Xmltable_column_option_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmltable_column_option_el.
    def enterXmltable_column_option_el(self, ctx:PostgreSQLParser.Xmltable_column_option_elContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmltable_column_option_el.
    def exitXmltable_column_option_el(self, ctx:PostgreSQLParser.Xmltable_column_option_elContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_namespace_list.
    def enterXml_namespace_list(self, ctx:PostgreSQLParser.Xml_namespace_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_namespace_list.
    def exitXml_namespace_list(self, ctx:PostgreSQLParser.Xml_namespace_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_namespace_el.
    def enterXml_namespace_el(self, ctx:PostgreSQLParser.Xml_namespace_elContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_namespace_el.
    def exitXml_namespace_el(self, ctx:PostgreSQLParser.Xml_namespace_elContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#typename.
    def enterTypename(self, ctx:PostgreSQLParser.TypenameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#typename.
    def exitTypename(self, ctx:PostgreSQLParser.TypenameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_array_bounds.
    def enterOpt_array_bounds(self, ctx:PostgreSQLParser.Opt_array_boundsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_array_bounds.
    def exitOpt_array_bounds(self, ctx:PostgreSQLParser.Opt_array_boundsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#simpletypename.
    def enterSimpletypename(self, ctx:PostgreSQLParser.SimpletypenameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#simpletypename.
    def exitSimpletypename(self, ctx:PostgreSQLParser.SimpletypenameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#consttypename.
    def enterConsttypename(self, ctx:PostgreSQLParser.ConsttypenameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#consttypename.
    def exitConsttypename(self, ctx:PostgreSQLParser.ConsttypenameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#generictype.
    def enterGenerictype(self, ctx:PostgreSQLParser.GenerictypeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#generictype.
    def exitGenerictype(self, ctx:PostgreSQLParser.GenerictypeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_type_modifiers.
    def enterOpt_type_modifiers(self, ctx:PostgreSQLParser.Opt_type_modifiersContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_type_modifiers.
    def exitOpt_type_modifiers(self, ctx:PostgreSQLParser.Opt_type_modifiersContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#numeric.
    def enterNumeric(self, ctx:PostgreSQLParser.NumericContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#numeric.
    def exitNumeric(self, ctx:PostgreSQLParser.NumericContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_float.
    def enterOpt_float(self, ctx:PostgreSQLParser.Opt_floatContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_float.
    def exitOpt_float(self, ctx:PostgreSQLParser.Opt_floatContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#bit.
    def enterBit(self, ctx:PostgreSQLParser.BitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#bit.
    def exitBit(self, ctx:PostgreSQLParser.BitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constbit.
    def enterConstbit(self, ctx:PostgreSQLParser.ConstbitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constbit.
    def exitConstbit(self, ctx:PostgreSQLParser.ConstbitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#bitwithlength.
    def enterBitwithlength(self, ctx:PostgreSQLParser.BitwithlengthContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#bitwithlength.
    def exitBitwithlength(self, ctx:PostgreSQLParser.BitwithlengthContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#bitwithoutlength.
    def enterBitwithoutlength(self, ctx:PostgreSQLParser.BitwithoutlengthContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#bitwithoutlength.
    def exitBitwithoutlength(self, ctx:PostgreSQLParser.BitwithoutlengthContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#character.
    def enterCharacter(self, ctx:PostgreSQLParser.CharacterContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#character.
    def exitCharacter(self, ctx:PostgreSQLParser.CharacterContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constcharacter.
    def enterConstcharacter(self, ctx:PostgreSQLParser.ConstcharacterContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constcharacter.
    def exitConstcharacter(self, ctx:PostgreSQLParser.ConstcharacterContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#character_c.
    def enterCharacter_c(self, ctx:PostgreSQLParser.Character_cContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#character_c.
    def exitCharacter_c(self, ctx:PostgreSQLParser.Character_cContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_varying.
    def enterOpt_varying(self, ctx:PostgreSQLParser.Opt_varyingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_varying.
    def exitOpt_varying(self, ctx:PostgreSQLParser.Opt_varyingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constdatetime.
    def enterConstdatetime(self, ctx:PostgreSQLParser.ConstdatetimeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constdatetime.
    def exitConstdatetime(self, ctx:PostgreSQLParser.ConstdatetimeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#constinterval.
    def enterConstinterval(self, ctx:PostgreSQLParser.ConstintervalContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#constinterval.
    def exitConstinterval(self, ctx:PostgreSQLParser.ConstintervalContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_timezone.
    def enterOpt_timezone(self, ctx:PostgreSQLParser.Opt_timezoneContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_timezone.
    def exitOpt_timezone(self, ctx:PostgreSQLParser.Opt_timezoneContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_interval.
    def enterOpt_interval(self, ctx:PostgreSQLParser.Opt_intervalContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_interval.
    def exitOpt_interval(self, ctx:PostgreSQLParser.Opt_intervalContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#interval_second.
    def enterInterval_second(self, ctx:PostgreSQLParser.Interval_secondContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#interval_second.
    def exitInterval_second(self, ctx:PostgreSQLParser.Interval_secondContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_escape.
    def enterOpt_escape(self, ctx:PostgreSQLParser.Opt_escapeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_escape.
    def exitOpt_escape(self, ctx:PostgreSQLParser.Opt_escapeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr.
    def enterA_expr(self, ctx:PostgreSQLParser.A_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr.
    def exitA_expr(self, ctx:PostgreSQLParser.A_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_qual.
    def enterA_expr_qual(self, ctx:PostgreSQLParser.A_expr_qualContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_qual.
    def exitA_expr_qual(self, ctx:PostgreSQLParser.A_expr_qualContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_lessless.
    def enterA_expr_lessless(self, ctx:PostgreSQLParser.A_expr_lesslessContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_lessless.
    def exitA_expr_lessless(self, ctx:PostgreSQLParser.A_expr_lesslessContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_or.
    def enterA_expr_or(self, ctx:PostgreSQLParser.A_expr_orContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_or.
    def exitA_expr_or(self, ctx:PostgreSQLParser.A_expr_orContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_and.
    def enterA_expr_and(self, ctx:PostgreSQLParser.A_expr_andContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_and.
    def exitA_expr_and(self, ctx:PostgreSQLParser.A_expr_andContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_between.
    def enterA_expr_between(self, ctx:PostgreSQLParser.A_expr_betweenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_between.
    def exitA_expr_between(self, ctx:PostgreSQLParser.A_expr_betweenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_in.
    def enterA_expr_in(self, ctx:PostgreSQLParser.A_expr_inContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_in.
    def exitA_expr_in(self, ctx:PostgreSQLParser.A_expr_inContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_unary_not.
    def enterA_expr_unary_not(self, ctx:PostgreSQLParser.A_expr_unary_notContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_unary_not.
    def exitA_expr_unary_not(self, ctx:PostgreSQLParser.A_expr_unary_notContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_isnull.
    def enterA_expr_isnull(self, ctx:PostgreSQLParser.A_expr_isnullContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_isnull.
    def exitA_expr_isnull(self, ctx:PostgreSQLParser.A_expr_isnullContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_is_not.
    def enterA_expr_is_not(self, ctx:PostgreSQLParser.A_expr_is_notContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_is_not.
    def exitA_expr_is_not(self, ctx:PostgreSQLParser.A_expr_is_notContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_compare.
    def enterA_expr_compare(self, ctx:PostgreSQLParser.A_expr_compareContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_compare.
    def exitA_expr_compare(self, ctx:PostgreSQLParser.A_expr_compareContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_like.
    def enterA_expr_like(self, ctx:PostgreSQLParser.A_expr_likeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_like.
    def exitA_expr_like(self, ctx:PostgreSQLParser.A_expr_likeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_qual_op.
    def enterA_expr_qual_op(self, ctx:PostgreSQLParser.A_expr_qual_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_qual_op.
    def exitA_expr_qual_op(self, ctx:PostgreSQLParser.A_expr_qual_opContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_unary_qualop.
    def enterA_expr_unary_qualop(self, ctx:PostgreSQLParser.A_expr_unary_qualopContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_unary_qualop.
    def exitA_expr_unary_qualop(self, ctx:PostgreSQLParser.A_expr_unary_qualopContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_add.
    def enterA_expr_add(self, ctx:PostgreSQLParser.A_expr_addContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_add.
    def exitA_expr_add(self, ctx:PostgreSQLParser.A_expr_addContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_mul.
    def enterA_expr_mul(self, ctx:PostgreSQLParser.A_expr_mulContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_mul.
    def exitA_expr_mul(self, ctx:PostgreSQLParser.A_expr_mulContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_caret.
    def enterA_expr_caret(self, ctx:PostgreSQLParser.A_expr_caretContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_caret.
    def exitA_expr_caret(self, ctx:PostgreSQLParser.A_expr_caretContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_unary_sign.
    def enterA_expr_unary_sign(self, ctx:PostgreSQLParser.A_expr_unary_signContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_unary_sign.
    def exitA_expr_unary_sign(self, ctx:PostgreSQLParser.A_expr_unary_signContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_at_time_zone.
    def enterA_expr_at_time_zone(self, ctx:PostgreSQLParser.A_expr_at_time_zoneContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_at_time_zone.
    def exitA_expr_at_time_zone(self, ctx:PostgreSQLParser.A_expr_at_time_zoneContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_collate.
    def enterA_expr_collate(self, ctx:PostgreSQLParser.A_expr_collateContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_collate.
    def exitA_expr_collate(self, ctx:PostgreSQLParser.A_expr_collateContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#a_expr_typecast.
    def enterA_expr_typecast(self, ctx:PostgreSQLParser.A_expr_typecastContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#a_expr_typecast.
    def exitA_expr_typecast(self, ctx:PostgreSQLParser.A_expr_typecastContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#b_expr.
    def enterB_expr(self, ctx:PostgreSQLParser.B_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#b_expr.
    def exitB_expr(self, ctx:PostgreSQLParser.B_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#c_expr_exists.
    def enterC_expr_exists(self, ctx:PostgreSQLParser.C_expr_existsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#c_expr_exists.
    def exitC_expr_exists(self, ctx:PostgreSQLParser.C_expr_existsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#c_expr_expr.
    def enterC_expr_expr(self, ctx:PostgreSQLParser.C_expr_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#c_expr_expr.
    def exitC_expr_expr(self, ctx:PostgreSQLParser.C_expr_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#c_expr_case.
    def enterC_expr_case(self, ctx:PostgreSQLParser.C_expr_caseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#c_expr_case.
    def exitC_expr_case(self, ctx:PostgreSQLParser.C_expr_caseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsqlvariablename.
    def enterPlsqlvariablename(self, ctx:PostgreSQLParser.PlsqlvariablenameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsqlvariablename.
    def exitPlsqlvariablename(self, ctx:PostgreSQLParser.PlsqlvariablenameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_application.
    def enterFunc_application(self, ctx:PostgreSQLParser.Func_applicationContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_application.
    def exitFunc_application(self, ctx:PostgreSQLParser.Func_applicationContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_expr.
    def enterFunc_expr(self, ctx:PostgreSQLParser.Func_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_expr.
    def exitFunc_expr(self, ctx:PostgreSQLParser.Func_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_expr_windowless.
    def enterFunc_expr_windowless(self, ctx:PostgreSQLParser.Func_expr_windowlessContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_expr_windowless.
    def exitFunc_expr_windowless(self, ctx:PostgreSQLParser.Func_expr_windowlessContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_expr_common_subexpr.
    def enterFunc_expr_common_subexpr(self, ctx:PostgreSQLParser.Func_expr_common_subexprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_expr_common_subexpr.
    def exitFunc_expr_common_subexpr(self, ctx:PostgreSQLParser.Func_expr_common_subexprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_root_version.
    def enterXml_root_version(self, ctx:PostgreSQLParser.Xml_root_versionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_root_version.
    def exitXml_root_version(self, ctx:PostgreSQLParser.Xml_root_versionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_xml_root_standalone.
    def enterOpt_xml_root_standalone(self, ctx:PostgreSQLParser.Opt_xml_root_standaloneContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_xml_root_standalone.
    def exitOpt_xml_root_standalone(self, ctx:PostgreSQLParser.Opt_xml_root_standaloneContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_attributes.
    def enterXml_attributes(self, ctx:PostgreSQLParser.Xml_attributesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_attributes.
    def exitXml_attributes(self, ctx:PostgreSQLParser.Xml_attributesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_attribute_list.
    def enterXml_attribute_list(self, ctx:PostgreSQLParser.Xml_attribute_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_attribute_list.
    def exitXml_attribute_list(self, ctx:PostgreSQLParser.Xml_attribute_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_attribute_el.
    def enterXml_attribute_el(self, ctx:PostgreSQLParser.Xml_attribute_elContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_attribute_el.
    def exitXml_attribute_el(self, ctx:PostgreSQLParser.Xml_attribute_elContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#document_or_content.
    def enterDocument_or_content(self, ctx:PostgreSQLParser.Document_or_contentContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#document_or_content.
    def exitDocument_or_content(self, ctx:PostgreSQLParser.Document_or_contentContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_whitespace_option.
    def enterXml_whitespace_option(self, ctx:PostgreSQLParser.Xml_whitespace_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_whitespace_option.
    def exitXml_whitespace_option(self, ctx:PostgreSQLParser.Xml_whitespace_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xmlexists_argument.
    def enterXmlexists_argument(self, ctx:PostgreSQLParser.Xmlexists_argumentContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xmlexists_argument.
    def exitXmlexists_argument(self, ctx:PostgreSQLParser.Xmlexists_argumentContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xml_passing_mech.
    def enterXml_passing_mech(self, ctx:PostgreSQLParser.Xml_passing_mechContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xml_passing_mech.
    def exitXml_passing_mech(self, ctx:PostgreSQLParser.Xml_passing_mechContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#within_group_clause.
    def enterWithin_group_clause(self, ctx:PostgreSQLParser.Within_group_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#within_group_clause.
    def exitWithin_group_clause(self, ctx:PostgreSQLParser.Within_group_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#filter_clause.
    def enterFilter_clause(self, ctx:PostgreSQLParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#filter_clause.
    def exitFilter_clause(self, ctx:PostgreSQLParser.Filter_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#window_clause.
    def enterWindow_clause(self, ctx:PostgreSQLParser.Window_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#window_clause.
    def exitWindow_clause(self, ctx:PostgreSQLParser.Window_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#window_definition_list.
    def enterWindow_definition_list(self, ctx:PostgreSQLParser.Window_definition_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#window_definition_list.
    def exitWindow_definition_list(self, ctx:PostgreSQLParser.Window_definition_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#window_definition.
    def enterWindow_definition(self, ctx:PostgreSQLParser.Window_definitionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#window_definition.
    def exitWindow_definition(self, ctx:PostgreSQLParser.Window_definitionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#over_clause.
    def enterOver_clause(self, ctx:PostgreSQLParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#over_clause.
    def exitOver_clause(self, ctx:PostgreSQLParser.Over_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#window_specification.
    def enterWindow_specification(self, ctx:PostgreSQLParser.Window_specificationContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#window_specification.
    def exitWindow_specification(self, ctx:PostgreSQLParser.Window_specificationContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_existing_window_name.
    def enterOpt_existing_window_name(self, ctx:PostgreSQLParser.Opt_existing_window_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_existing_window_name.
    def exitOpt_existing_window_name(self, ctx:PostgreSQLParser.Opt_existing_window_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_partition_clause.
    def enterOpt_partition_clause(self, ctx:PostgreSQLParser.Opt_partition_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_partition_clause.
    def exitOpt_partition_clause(self, ctx:PostgreSQLParser.Opt_partition_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_frame_clause.
    def enterOpt_frame_clause(self, ctx:PostgreSQLParser.Opt_frame_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_frame_clause.
    def exitOpt_frame_clause(self, ctx:PostgreSQLParser.Opt_frame_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#frame_extent.
    def enterFrame_extent(self, ctx:PostgreSQLParser.Frame_extentContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#frame_extent.
    def exitFrame_extent(self, ctx:PostgreSQLParser.Frame_extentContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#frame_bound.
    def enterFrame_bound(self, ctx:PostgreSQLParser.Frame_boundContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#frame_bound.
    def exitFrame_bound(self, ctx:PostgreSQLParser.Frame_boundContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_window_exclusion_clause.
    def enterOpt_window_exclusion_clause(self, ctx:PostgreSQLParser.Opt_window_exclusion_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_window_exclusion_clause.
    def exitOpt_window_exclusion_clause(self, ctx:PostgreSQLParser.Opt_window_exclusion_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#row.
    def enterRow(self, ctx:PostgreSQLParser.RowContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#row.
    def exitRow(self, ctx:PostgreSQLParser.RowContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#explicit_row.
    def enterExplicit_row(self, ctx:PostgreSQLParser.Explicit_rowContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#explicit_row.
    def exitExplicit_row(self, ctx:PostgreSQLParser.Explicit_rowContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#implicit_row.
    def enterImplicit_row(self, ctx:PostgreSQLParser.Implicit_rowContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#implicit_row.
    def exitImplicit_row(self, ctx:PostgreSQLParser.Implicit_rowContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sub_type.
    def enterSub_type(self, ctx:PostgreSQLParser.Sub_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sub_type.
    def exitSub_type(self, ctx:PostgreSQLParser.Sub_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#all_op.
    def enterAll_op(self, ctx:PostgreSQLParser.All_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#all_op.
    def exitAll_op(self, ctx:PostgreSQLParser.All_opContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#mathop.
    def enterMathop(self, ctx:PostgreSQLParser.MathopContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#mathop.
    def exitMathop(self, ctx:PostgreSQLParser.MathopContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#qual_op.
    def enterQual_op(self, ctx:PostgreSQLParser.Qual_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#qual_op.
    def exitQual_op(self, ctx:PostgreSQLParser.Qual_opContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#qual_all_op.
    def enterQual_all_op(self, ctx:PostgreSQLParser.Qual_all_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#qual_all_op.
    def exitQual_all_op(self, ctx:PostgreSQLParser.Qual_all_opContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#subquery_Op.
    def enterSubquery_Op(self, ctx:PostgreSQLParser.Subquery_OpContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#subquery_Op.
    def exitSubquery_Op(self, ctx:PostgreSQLParser.Subquery_OpContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expr_list.
    def enterExpr_list(self, ctx:PostgreSQLParser.Expr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expr_list.
    def exitExpr_list(self, ctx:PostgreSQLParser.Expr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_arg_list.
    def enterFunc_arg_list(self, ctx:PostgreSQLParser.Func_arg_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_arg_list.
    def exitFunc_arg_list(self, ctx:PostgreSQLParser.Func_arg_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_arg_expr.
    def enterFunc_arg_expr(self, ctx:PostgreSQLParser.Func_arg_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_arg_expr.
    def exitFunc_arg_expr(self, ctx:PostgreSQLParser.Func_arg_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#type_list.
    def enterType_list(self, ctx:PostgreSQLParser.Type_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#type_list.
    def exitType_list(self, ctx:PostgreSQLParser.Type_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#array_expr.
    def enterArray_expr(self, ctx:PostgreSQLParser.Array_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#array_expr.
    def exitArray_expr(self, ctx:PostgreSQLParser.Array_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#array_expr_list.
    def enterArray_expr_list(self, ctx:PostgreSQLParser.Array_expr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#array_expr_list.
    def exitArray_expr_list(self, ctx:PostgreSQLParser.Array_expr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#extract_list.
    def enterExtract_list(self, ctx:PostgreSQLParser.Extract_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#extract_list.
    def exitExtract_list(self, ctx:PostgreSQLParser.Extract_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#extract_arg.
    def enterExtract_arg(self, ctx:PostgreSQLParser.Extract_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#extract_arg.
    def exitExtract_arg(self, ctx:PostgreSQLParser.Extract_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#unicode_normal_form.
    def enterUnicode_normal_form(self, ctx:PostgreSQLParser.Unicode_normal_formContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#unicode_normal_form.
    def exitUnicode_normal_form(self, ctx:PostgreSQLParser.Unicode_normal_formContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#overlay_list.
    def enterOverlay_list(self, ctx:PostgreSQLParser.Overlay_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#overlay_list.
    def exitOverlay_list(self, ctx:PostgreSQLParser.Overlay_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#position_list.
    def enterPosition_list(self, ctx:PostgreSQLParser.Position_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#position_list.
    def exitPosition_list(self, ctx:PostgreSQLParser.Position_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#substr_list.
    def enterSubstr_list(self, ctx:PostgreSQLParser.Substr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#substr_list.
    def exitSubstr_list(self, ctx:PostgreSQLParser.Substr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#trim_list.
    def enterTrim_list(self, ctx:PostgreSQLParser.Trim_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#trim_list.
    def exitTrim_list(self, ctx:PostgreSQLParser.Trim_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#in_expr_select.
    def enterIn_expr_select(self, ctx:PostgreSQLParser.In_expr_selectContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#in_expr_select.
    def exitIn_expr_select(self, ctx:PostgreSQLParser.In_expr_selectContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#in_expr_list.
    def enterIn_expr_list(self, ctx:PostgreSQLParser.In_expr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#in_expr_list.
    def exitIn_expr_list(self, ctx:PostgreSQLParser.In_expr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#case_expr.
    def enterCase_expr(self, ctx:PostgreSQLParser.Case_exprContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#case_expr.
    def exitCase_expr(self, ctx:PostgreSQLParser.Case_exprContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#when_clause_list.
    def enterWhen_clause_list(self, ctx:PostgreSQLParser.When_clause_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#when_clause_list.
    def exitWhen_clause_list(self, ctx:PostgreSQLParser.When_clause_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#when_clause.
    def enterWhen_clause(self, ctx:PostgreSQLParser.When_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#when_clause.
    def exitWhen_clause(self, ctx:PostgreSQLParser.When_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#case_default.
    def enterCase_default(self, ctx:PostgreSQLParser.Case_defaultContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#case_default.
    def exitCase_default(self, ctx:PostgreSQLParser.Case_defaultContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#case_arg.
    def enterCase_arg(self, ctx:PostgreSQLParser.Case_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#case_arg.
    def exitCase_arg(self, ctx:PostgreSQLParser.Case_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnref.
    def enterColumnref(self, ctx:PostgreSQLParser.ColumnrefContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnref.
    def exitColumnref(self, ctx:PostgreSQLParser.ColumnrefContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#indirection_el.
    def enterIndirection_el(self, ctx:PostgreSQLParser.Indirection_elContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#indirection_el.
    def exitIndirection_el(self, ctx:PostgreSQLParser.Indirection_elContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_slice_bound.
    def enterOpt_slice_bound(self, ctx:PostgreSQLParser.Opt_slice_boundContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_slice_bound.
    def exitOpt_slice_bound(self, ctx:PostgreSQLParser.Opt_slice_boundContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#indirection.
    def enterIndirection(self, ctx:PostgreSQLParser.IndirectionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#indirection.
    def exitIndirection(self, ctx:PostgreSQLParser.IndirectionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_indirection.
    def enterOpt_indirection(self, ctx:PostgreSQLParser.Opt_indirectionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_indirection.
    def exitOpt_indirection(self, ctx:PostgreSQLParser.Opt_indirectionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_target_list.
    def enterOpt_target_list(self, ctx:PostgreSQLParser.Opt_target_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_target_list.
    def exitOpt_target_list(self, ctx:PostgreSQLParser.Opt_target_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#target_list.
    def enterTarget_list(self, ctx:PostgreSQLParser.Target_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#target_list.
    def exitTarget_list(self, ctx:PostgreSQLParser.Target_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#target_label.
    def enterTarget_label(self, ctx:PostgreSQLParser.Target_labelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#target_label.
    def exitTarget_label(self, ctx:PostgreSQLParser.Target_labelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#target_star.
    def enterTarget_star(self, ctx:PostgreSQLParser.Target_starContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#target_star.
    def exitTarget_star(self, ctx:PostgreSQLParser.Target_starContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#qualified_name_list.
    def enterQualified_name_list(self, ctx:PostgreSQLParser.Qualified_name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#qualified_name_list.
    def exitQualified_name_list(self, ctx:PostgreSQLParser.Qualified_name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#qualified_name.
    def enterQualified_name(self, ctx:PostgreSQLParser.Qualified_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#qualified_name.
    def exitQualified_name(self, ctx:PostgreSQLParser.Qualified_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#name_list.
    def enterName_list(self, ctx:PostgreSQLParser.Name_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#name_list.
    def exitName_list(self, ctx:PostgreSQLParser.Name_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#name.
    def enterName(self, ctx:PostgreSQLParser.NameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#name.
    def exitName(self, ctx:PostgreSQLParser.NameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#attr_name.
    def enterAttr_name(self, ctx:PostgreSQLParser.Attr_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#attr_name.
    def exitAttr_name(self, ctx:PostgreSQLParser.Attr_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#file_name.
    def enterFile_name(self, ctx:PostgreSQLParser.File_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#file_name.
    def exitFile_name(self, ctx:PostgreSQLParser.File_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#func_name.
    def enterFunc_name(self, ctx:PostgreSQLParser.Func_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#func_name.
    def exitFunc_name(self, ctx:PostgreSQLParser.Func_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aexprconst.
    def enterAexprconst(self, ctx:PostgreSQLParser.AexprconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aexprconst.
    def exitAexprconst(self, ctx:PostgreSQLParser.AexprconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#xconst.
    def enterXconst(self, ctx:PostgreSQLParser.XconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#xconst.
    def exitXconst(self, ctx:PostgreSQLParser.XconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#bconst.
    def enterBconst(self, ctx:PostgreSQLParser.BconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#bconst.
    def exitBconst(self, ctx:PostgreSQLParser.BconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#fconst.
    def enterFconst(self, ctx:PostgreSQLParser.FconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#fconst.
    def exitFconst(self, ctx:PostgreSQLParser.FconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#iconst.
    def enterIconst(self, ctx:PostgreSQLParser.IconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#iconst.
    def exitIconst(self, ctx:PostgreSQLParser.IconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sconst.
    def enterSconst(self, ctx:PostgreSQLParser.SconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sconst.
    def exitSconst(self, ctx:PostgreSQLParser.SconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#anysconst.
    def enterAnysconst(self, ctx:PostgreSQLParser.AnysconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#anysconst.
    def exitAnysconst(self, ctx:PostgreSQLParser.AnysconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_uescape.
    def enterOpt_uescape(self, ctx:PostgreSQLParser.Opt_uescapeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_uescape.
    def exitOpt_uescape(self, ctx:PostgreSQLParser.Opt_uescapeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#signediconst.
    def enterSignediconst(self, ctx:PostgreSQLParser.SignediconstContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#signediconst.
    def exitSignediconst(self, ctx:PostgreSQLParser.SignediconstContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#roleid.
    def enterRoleid(self, ctx:PostgreSQLParser.RoleidContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#roleid.
    def exitRoleid(self, ctx:PostgreSQLParser.RoleidContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#rolespec.
    def enterRolespec(self, ctx:PostgreSQLParser.RolespecContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#rolespec.
    def exitRolespec(self, ctx:PostgreSQLParser.RolespecContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#role_list.
    def enterRole_list(self, ctx:PostgreSQLParser.Role_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#role_list.
    def exitRole_list(self, ctx:PostgreSQLParser.Role_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#colid.
    def enterColid(self, ctx:PostgreSQLParser.ColidContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#colid.
    def exitColid(self, ctx:PostgreSQLParser.ColidContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_alias.
    def enterTable_alias(self, ctx:PostgreSQLParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_alias.
    def exitTable_alias(self, ctx:PostgreSQLParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#type_function_name.
    def enterType_function_name(self, ctx:PostgreSQLParser.Type_function_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#type_function_name.
    def exitType_function_name(self, ctx:PostgreSQLParser.Type_function_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#nonreservedword.
    def enterNonreservedword(self, ctx:PostgreSQLParser.NonreservedwordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#nonreservedword.
    def exitNonreservedword(self, ctx:PostgreSQLParser.NonreservedwordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#collabel.
    def enterCollabel(self, ctx:PostgreSQLParser.CollabelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#collabel.
    def exitCollabel(self, ctx:PostgreSQLParser.CollabelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#identifier.
    def enterIdentifier(self, ctx:PostgreSQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#identifier.
    def exitIdentifier(self, ctx:PostgreSQLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsqlidentifier.
    def enterPlsqlidentifier(self, ctx:PostgreSQLParser.PlsqlidentifierContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsqlidentifier.
    def exitPlsqlidentifier(self, ctx:PostgreSQLParser.PlsqlidentifierContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#unreserved_keyword.
    def enterUnreserved_keyword(self, ctx:PostgreSQLParser.Unreserved_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#unreserved_keyword.
    def exitUnreserved_keyword(self, ctx:PostgreSQLParser.Unreserved_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#col_name_keyword.
    def enterCol_name_keyword(self, ctx:PostgreSQLParser.Col_name_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#col_name_keyword.
    def exitCol_name_keyword(self, ctx:PostgreSQLParser.Col_name_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#type_func_name_keyword.
    def enterType_func_name_keyword(self, ctx:PostgreSQLParser.Type_func_name_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#type_func_name_keyword.
    def exitType_func_name_keyword(self, ctx:PostgreSQLParser.Type_func_name_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#reserved_keyword.
    def enterReserved_keyword(self, ctx:PostgreSQLParser.Reserved_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#reserved_keyword.
    def exitReserved_keyword(self, ctx:PostgreSQLParser.Reserved_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#builtin_function_name.
    def enterBuiltin_function_name(self, ctx:PostgreSQLParser.Builtin_function_nameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#builtin_function_name.
    def exitBuiltin_function_name(self, ctx:PostgreSQLParser.Builtin_function_nameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#pl_function.
    def enterPl_function(self, ctx:PostgreSQLParser.Pl_functionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#pl_function.
    def exitPl_function(self, ctx:PostgreSQLParser.Pl_functionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#comp_options.
    def enterComp_options(self, ctx:PostgreSQLParser.Comp_optionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#comp_options.
    def exitComp_options(self, ctx:PostgreSQLParser.Comp_optionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#comp_option.
    def enterComp_option(self, ctx:PostgreSQLParser.Comp_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#comp_option.
    def exitComp_option(self, ctx:PostgreSQLParser.Comp_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sharp.
    def enterSharp(self, ctx:PostgreSQLParser.SharpContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sharp.
    def exitSharp(self, ctx:PostgreSQLParser.SharpContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#option_value.
    def enterOption_value(self, ctx:PostgreSQLParser.Option_valueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#option_value.
    def exitOption_value(self, ctx:PostgreSQLParser.Option_valueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_semi.
    def enterOpt_semi(self, ctx:PostgreSQLParser.Opt_semiContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_semi.
    def exitOpt_semi(self, ctx:PostgreSQLParser.Opt_semiContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#pl_block.
    def enterPl_block(self, ctx:PostgreSQLParser.Pl_blockContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#pl_block.
    def exitPl_block(self, ctx:PostgreSQLParser.Pl_blockContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_sect.
    def enterDecl_sect(self, ctx:PostgreSQLParser.Decl_sectContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_sect.
    def exitDecl_sect(self, ctx:PostgreSQLParser.Decl_sectContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_start.
    def enterDecl_start(self, ctx:PostgreSQLParser.Decl_startContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_start.
    def exitDecl_start(self, ctx:PostgreSQLParser.Decl_startContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_stmts.
    def enterDecl_stmts(self, ctx:PostgreSQLParser.Decl_stmtsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_stmts.
    def exitDecl_stmts(self, ctx:PostgreSQLParser.Decl_stmtsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#label_decl.
    def enterLabel_decl(self, ctx:PostgreSQLParser.Label_declContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#label_decl.
    def exitLabel_decl(self, ctx:PostgreSQLParser.Label_declContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_stmt.
    def enterDecl_stmt(self, ctx:PostgreSQLParser.Decl_stmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_stmt.
    def exitDecl_stmt(self, ctx:PostgreSQLParser.Decl_stmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_statement.
    def enterDecl_statement(self, ctx:PostgreSQLParser.Decl_statementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_statement.
    def exitDecl_statement(self, ctx:PostgreSQLParser.Decl_statementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_scrollable.
    def enterOpt_scrollable(self, ctx:PostgreSQLParser.Opt_scrollableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_scrollable.
    def exitOpt_scrollable(self, ctx:PostgreSQLParser.Opt_scrollableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_cursor_query.
    def enterDecl_cursor_query(self, ctx:PostgreSQLParser.Decl_cursor_queryContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_cursor_query.
    def exitDecl_cursor_query(self, ctx:PostgreSQLParser.Decl_cursor_queryContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_cursor_args.
    def enterDecl_cursor_args(self, ctx:PostgreSQLParser.Decl_cursor_argsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_cursor_args.
    def exitDecl_cursor_args(self, ctx:PostgreSQLParser.Decl_cursor_argsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_cursor_arglist.
    def enterDecl_cursor_arglist(self, ctx:PostgreSQLParser.Decl_cursor_arglistContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_cursor_arglist.
    def exitDecl_cursor_arglist(self, ctx:PostgreSQLParser.Decl_cursor_arglistContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_cursor_arg.
    def enterDecl_cursor_arg(self, ctx:PostgreSQLParser.Decl_cursor_argContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_cursor_arg.
    def exitDecl_cursor_arg(self, ctx:PostgreSQLParser.Decl_cursor_argContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_is_for.
    def enterDecl_is_for(self, ctx:PostgreSQLParser.Decl_is_forContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_is_for.
    def exitDecl_is_for(self, ctx:PostgreSQLParser.Decl_is_forContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_aliasitem.
    def enterDecl_aliasitem(self, ctx:PostgreSQLParser.Decl_aliasitemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_aliasitem.
    def exitDecl_aliasitem(self, ctx:PostgreSQLParser.Decl_aliasitemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_varname.
    def enterDecl_varname(self, ctx:PostgreSQLParser.Decl_varnameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_varname.
    def exitDecl_varname(self, ctx:PostgreSQLParser.Decl_varnameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_const.
    def enterDecl_const(self, ctx:PostgreSQLParser.Decl_constContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_const.
    def exitDecl_const(self, ctx:PostgreSQLParser.Decl_constContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_datatype.
    def enterDecl_datatype(self, ctx:PostgreSQLParser.Decl_datatypeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_datatype.
    def exitDecl_datatype(self, ctx:PostgreSQLParser.Decl_datatypeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_collate.
    def enterDecl_collate(self, ctx:PostgreSQLParser.Decl_collateContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_collate.
    def exitDecl_collate(self, ctx:PostgreSQLParser.Decl_collateContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_notnull.
    def enterDecl_notnull(self, ctx:PostgreSQLParser.Decl_notnullContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_notnull.
    def exitDecl_notnull(self, ctx:PostgreSQLParser.Decl_notnullContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_defval.
    def enterDecl_defval(self, ctx:PostgreSQLParser.Decl_defvalContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_defval.
    def exitDecl_defval(self, ctx:PostgreSQLParser.Decl_defvalContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#decl_defkey.
    def enterDecl_defkey(self, ctx:PostgreSQLParser.Decl_defkeyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#decl_defkey.
    def exitDecl_defkey(self, ctx:PostgreSQLParser.Decl_defkeyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#assign_operator.
    def enterAssign_operator(self, ctx:PostgreSQLParser.Assign_operatorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#assign_operator.
    def exitAssign_operator(self, ctx:PostgreSQLParser.Assign_operatorContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_sect.
    def enterProc_sect(self, ctx:PostgreSQLParser.Proc_sectContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_sect.
    def exitProc_sect(self, ctx:PostgreSQLParser.Proc_sectContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_stmt.
    def enterProc_stmt(self, ctx:PostgreSQLParser.Proc_stmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_stmt.
    def exitProc_stmt(self, ctx:PostgreSQLParser.Proc_stmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_perform.
    def enterStmt_perform(self, ctx:PostgreSQLParser.Stmt_performContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_perform.
    def exitStmt_perform(self, ctx:PostgreSQLParser.Stmt_performContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_call.
    def enterStmt_call(self, ctx:PostgreSQLParser.Stmt_callContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_call.
    def exitStmt_call(self, ctx:PostgreSQLParser.Stmt_callContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_expr_list.
    def enterOpt_expr_list(self, ctx:PostgreSQLParser.Opt_expr_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_expr_list.
    def exitOpt_expr_list(self, ctx:PostgreSQLParser.Opt_expr_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_assign.
    def enterStmt_assign(self, ctx:PostgreSQLParser.Stmt_assignContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_assign.
    def exitStmt_assign(self, ctx:PostgreSQLParser.Stmt_assignContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_getdiag.
    def enterStmt_getdiag(self, ctx:PostgreSQLParser.Stmt_getdiagContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_getdiag.
    def exitStmt_getdiag(self, ctx:PostgreSQLParser.Stmt_getdiagContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#getdiag_area_opt.
    def enterGetdiag_area_opt(self, ctx:PostgreSQLParser.Getdiag_area_optContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#getdiag_area_opt.
    def exitGetdiag_area_opt(self, ctx:PostgreSQLParser.Getdiag_area_optContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#getdiag_list.
    def enterGetdiag_list(self, ctx:PostgreSQLParser.Getdiag_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#getdiag_list.
    def exitGetdiag_list(self, ctx:PostgreSQLParser.Getdiag_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#getdiag_list_item.
    def enterGetdiag_list_item(self, ctx:PostgreSQLParser.Getdiag_list_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#getdiag_list_item.
    def exitGetdiag_list_item(self, ctx:PostgreSQLParser.Getdiag_list_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#getdiag_item.
    def enterGetdiag_item(self, ctx:PostgreSQLParser.Getdiag_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#getdiag_item.
    def exitGetdiag_item(self, ctx:PostgreSQLParser.Getdiag_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#getdiag_target.
    def enterGetdiag_target(self, ctx:PostgreSQLParser.Getdiag_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#getdiag_target.
    def exitGetdiag_target(self, ctx:PostgreSQLParser.Getdiag_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#assign_var.
    def enterAssign_var(self, ctx:PostgreSQLParser.Assign_varContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#assign_var.
    def exitAssign_var(self, ctx:PostgreSQLParser.Assign_varContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_if.
    def enterStmt_if(self, ctx:PostgreSQLParser.Stmt_ifContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_if.
    def exitStmt_if(self, ctx:PostgreSQLParser.Stmt_ifContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_elsifs.
    def enterStmt_elsifs(self, ctx:PostgreSQLParser.Stmt_elsifsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_elsifs.
    def exitStmt_elsifs(self, ctx:PostgreSQLParser.Stmt_elsifsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_else.
    def enterStmt_else(self, ctx:PostgreSQLParser.Stmt_elseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_else.
    def exitStmt_else(self, ctx:PostgreSQLParser.Stmt_elseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_case.
    def enterStmt_case(self, ctx:PostgreSQLParser.Stmt_caseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_case.
    def exitStmt_case(self, ctx:PostgreSQLParser.Stmt_caseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_expr_until_when.
    def enterOpt_expr_until_when(self, ctx:PostgreSQLParser.Opt_expr_until_whenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_expr_until_when.
    def exitOpt_expr_until_when(self, ctx:PostgreSQLParser.Opt_expr_until_whenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#case_when_list.
    def enterCase_when_list(self, ctx:PostgreSQLParser.Case_when_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#case_when_list.
    def exitCase_when_list(self, ctx:PostgreSQLParser.Case_when_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#case_when.
    def enterCase_when(self, ctx:PostgreSQLParser.Case_whenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#case_when.
    def exitCase_when(self, ctx:PostgreSQLParser.Case_whenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_case_else.
    def enterOpt_case_else(self, ctx:PostgreSQLParser.Opt_case_elseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_case_else.
    def exitOpt_case_else(self, ctx:PostgreSQLParser.Opt_case_elseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_loop.
    def enterStmt_loop(self, ctx:PostgreSQLParser.Stmt_loopContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_loop.
    def exitStmt_loop(self, ctx:PostgreSQLParser.Stmt_loopContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_while.
    def enterStmt_while(self, ctx:PostgreSQLParser.Stmt_whileContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_while.
    def exitStmt_while(self, ctx:PostgreSQLParser.Stmt_whileContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_for.
    def enterStmt_for(self, ctx:PostgreSQLParser.Stmt_forContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_for.
    def exitStmt_for(self, ctx:PostgreSQLParser.Stmt_forContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_control.
    def enterFor_control(self, ctx:PostgreSQLParser.For_controlContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_control.
    def exitFor_control(self, ctx:PostgreSQLParser.For_controlContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_for_using_expression.
    def enterOpt_for_using_expression(self, ctx:PostgreSQLParser.Opt_for_using_expressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_for_using_expression.
    def exitOpt_for_using_expression(self, ctx:PostgreSQLParser.Opt_for_using_expressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_cursor_parameters.
    def enterOpt_cursor_parameters(self, ctx:PostgreSQLParser.Opt_cursor_parametersContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_cursor_parameters.
    def exitOpt_cursor_parameters(self, ctx:PostgreSQLParser.Opt_cursor_parametersContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_reverse.
    def enterOpt_reverse(self, ctx:PostgreSQLParser.Opt_reverseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_reverse.
    def exitOpt_reverse(self, ctx:PostgreSQLParser.Opt_reverseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_by_expression.
    def enterOpt_by_expression(self, ctx:PostgreSQLParser.Opt_by_expressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_by_expression.
    def exitOpt_by_expression(self, ctx:PostgreSQLParser.Opt_by_expressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#for_variable.
    def enterFor_variable(self, ctx:PostgreSQLParser.For_variableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#for_variable.
    def exitFor_variable(self, ctx:PostgreSQLParser.For_variableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_foreach_a.
    def enterStmt_foreach_a(self, ctx:PostgreSQLParser.Stmt_foreach_aContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_foreach_a.
    def exitStmt_foreach_a(self, ctx:PostgreSQLParser.Stmt_foreach_aContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#foreach_slice.
    def enterForeach_slice(self, ctx:PostgreSQLParser.Foreach_sliceContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#foreach_slice.
    def exitForeach_slice(self, ctx:PostgreSQLParser.Foreach_sliceContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_exit.
    def enterStmt_exit(self, ctx:PostgreSQLParser.Stmt_exitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_exit.
    def exitStmt_exit(self, ctx:PostgreSQLParser.Stmt_exitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#exit_type.
    def enterExit_type(self, ctx:PostgreSQLParser.Exit_typeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#exit_type.
    def exitExit_type(self, ctx:PostgreSQLParser.Exit_typeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_return.
    def enterStmt_return(self, ctx:PostgreSQLParser.Stmt_returnContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_return.
    def exitStmt_return(self, ctx:PostgreSQLParser.Stmt_returnContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_return_result.
    def enterOpt_return_result(self, ctx:PostgreSQLParser.Opt_return_resultContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_return_result.
    def exitOpt_return_result(self, ctx:PostgreSQLParser.Opt_return_resultContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_raise.
    def enterStmt_raise(self, ctx:PostgreSQLParser.Stmt_raiseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_raise.
    def exitStmt_raise(self, ctx:PostgreSQLParser.Stmt_raiseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_stmt_raise_level.
    def enterOpt_stmt_raise_level(self, ctx:PostgreSQLParser.Opt_stmt_raise_levelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_stmt_raise_level.
    def exitOpt_stmt_raise_level(self, ctx:PostgreSQLParser.Opt_stmt_raise_levelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_raise_list.
    def enterOpt_raise_list(self, ctx:PostgreSQLParser.Opt_raise_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_raise_list.
    def exitOpt_raise_list(self, ctx:PostgreSQLParser.Opt_raise_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_raise_using.
    def enterOpt_raise_using(self, ctx:PostgreSQLParser.Opt_raise_usingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_raise_using.
    def exitOpt_raise_using(self, ctx:PostgreSQLParser.Opt_raise_usingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_raise_using_elem.
    def enterOpt_raise_using_elem(self, ctx:PostgreSQLParser.Opt_raise_using_elemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_raise_using_elem.
    def exitOpt_raise_using_elem(self, ctx:PostgreSQLParser.Opt_raise_using_elemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_raise_using_elem_list.
    def enterOpt_raise_using_elem_list(self, ctx:PostgreSQLParser.Opt_raise_using_elem_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_raise_using_elem_list.
    def exitOpt_raise_using_elem_list(self, ctx:PostgreSQLParser.Opt_raise_using_elem_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_assert.
    def enterStmt_assert(self, ctx:PostgreSQLParser.Stmt_assertContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_assert.
    def exitStmt_assert(self, ctx:PostgreSQLParser.Stmt_assertContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_stmt_assert_message.
    def enterOpt_stmt_assert_message(self, ctx:PostgreSQLParser.Opt_stmt_assert_messageContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_stmt_assert_message.
    def exitOpt_stmt_assert_message(self, ctx:PostgreSQLParser.Opt_stmt_assert_messageContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#loop_body.
    def enterLoop_body(self, ctx:PostgreSQLParser.Loop_bodyContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#loop_body.
    def exitLoop_body(self, ctx:PostgreSQLParser.Loop_bodyContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_execsql.
    def enterStmt_execsql(self, ctx:PostgreSQLParser.Stmt_execsqlContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_execsql.
    def exitStmt_execsql(self, ctx:PostgreSQLParser.Stmt_execsqlContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_dynexecute.
    def enterStmt_dynexecute(self, ctx:PostgreSQLParser.Stmt_dynexecuteContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_dynexecute.
    def exitStmt_dynexecute(self, ctx:PostgreSQLParser.Stmt_dynexecuteContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_execute_using.
    def enterOpt_execute_using(self, ctx:PostgreSQLParser.Opt_execute_usingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_execute_using.
    def exitOpt_execute_using(self, ctx:PostgreSQLParser.Opt_execute_usingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_execute_using_list.
    def enterOpt_execute_using_list(self, ctx:PostgreSQLParser.Opt_execute_using_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_execute_using_list.
    def exitOpt_execute_using_list(self, ctx:PostgreSQLParser.Opt_execute_using_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_execute_into.
    def enterOpt_execute_into(self, ctx:PostgreSQLParser.Opt_execute_intoContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_execute_into.
    def exitOpt_execute_into(self, ctx:PostgreSQLParser.Opt_execute_intoContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_open.
    def enterStmt_open(self, ctx:PostgreSQLParser.Stmt_openContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_open.
    def exitStmt_open(self, ctx:PostgreSQLParser.Stmt_openContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_open_bound_list_item.
    def enterOpt_open_bound_list_item(self, ctx:PostgreSQLParser.Opt_open_bound_list_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_open_bound_list_item.
    def exitOpt_open_bound_list_item(self, ctx:PostgreSQLParser.Opt_open_bound_list_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_open_bound_list.
    def enterOpt_open_bound_list(self, ctx:PostgreSQLParser.Opt_open_bound_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_open_bound_list.
    def exitOpt_open_bound_list(self, ctx:PostgreSQLParser.Opt_open_bound_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_open_using.
    def enterOpt_open_using(self, ctx:PostgreSQLParser.Opt_open_usingContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_open_using.
    def exitOpt_open_using(self, ctx:PostgreSQLParser.Opt_open_usingContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_scroll_option.
    def enterOpt_scroll_option(self, ctx:PostgreSQLParser.Opt_scroll_optionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_scroll_option.
    def exitOpt_scroll_option(self, ctx:PostgreSQLParser.Opt_scroll_optionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_scroll_option_no.
    def enterOpt_scroll_option_no(self, ctx:PostgreSQLParser.Opt_scroll_option_noContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_scroll_option_no.
    def exitOpt_scroll_option_no(self, ctx:PostgreSQLParser.Opt_scroll_option_noContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_fetch.
    def enterStmt_fetch(self, ctx:PostgreSQLParser.Stmt_fetchContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_fetch.
    def exitStmt_fetch(self, ctx:PostgreSQLParser.Stmt_fetchContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#into_target.
    def enterInto_target(self, ctx:PostgreSQLParser.Into_targetContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#into_target.
    def exitInto_target(self, ctx:PostgreSQLParser.Into_targetContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_cursor_from.
    def enterOpt_cursor_from(self, ctx:PostgreSQLParser.Opt_cursor_fromContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_cursor_from.
    def exitOpt_cursor_from(self, ctx:PostgreSQLParser.Opt_cursor_fromContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_fetch_direction.
    def enterOpt_fetch_direction(self, ctx:PostgreSQLParser.Opt_fetch_directionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_fetch_direction.
    def exitOpt_fetch_direction(self, ctx:PostgreSQLParser.Opt_fetch_directionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_move.
    def enterStmt_move(self, ctx:PostgreSQLParser.Stmt_moveContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_move.
    def exitStmt_move(self, ctx:PostgreSQLParser.Stmt_moveContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_close.
    def enterStmt_close(self, ctx:PostgreSQLParser.Stmt_closeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_close.
    def exitStmt_close(self, ctx:PostgreSQLParser.Stmt_closeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_null.
    def enterStmt_null(self, ctx:PostgreSQLParser.Stmt_nullContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_null.
    def exitStmt_null(self, ctx:PostgreSQLParser.Stmt_nullContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_commit.
    def enterStmt_commit(self, ctx:PostgreSQLParser.Stmt_commitContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_commit.
    def exitStmt_commit(self, ctx:PostgreSQLParser.Stmt_commitContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_rollback.
    def enterStmt_rollback(self, ctx:PostgreSQLParser.Stmt_rollbackContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_rollback.
    def exitStmt_rollback(self, ctx:PostgreSQLParser.Stmt_rollbackContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsql_opt_transaction_chain.
    def enterPlsql_opt_transaction_chain(self, ctx:PostgreSQLParser.Plsql_opt_transaction_chainContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsql_opt_transaction_chain.
    def exitPlsql_opt_transaction_chain(self, ctx:PostgreSQLParser.Plsql_opt_transaction_chainContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#stmt_set.
    def enterStmt_set(self, ctx:PostgreSQLParser.Stmt_setContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#stmt_set.
    def exitStmt_set(self, ctx:PostgreSQLParser.Stmt_setContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#cursor_variable.
    def enterCursor_variable(self, ctx:PostgreSQLParser.Cursor_variableContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#cursor_variable.
    def exitCursor_variable(self, ctx:PostgreSQLParser.Cursor_variableContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#exception_sect.
    def enterException_sect(self, ctx:PostgreSQLParser.Exception_sectContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#exception_sect.
    def exitException_sect(self, ctx:PostgreSQLParser.Exception_sectContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_exceptions.
    def enterProc_exceptions(self, ctx:PostgreSQLParser.Proc_exceptionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_exceptions.
    def exitProc_exceptions(self, ctx:PostgreSQLParser.Proc_exceptionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_exception.
    def enterProc_exception(self, ctx:PostgreSQLParser.Proc_exceptionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_exception.
    def exitProc_exception(self, ctx:PostgreSQLParser.Proc_exceptionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_conditions.
    def enterProc_conditions(self, ctx:PostgreSQLParser.Proc_conditionsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_conditions.
    def exitProc_conditions(self, ctx:PostgreSQLParser.Proc_conditionsContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#proc_condition.
    def enterProc_condition(self, ctx:PostgreSQLParser.Proc_conditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#proc_condition.
    def exitProc_condition(self, ctx:PostgreSQLParser.Proc_conditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_block_label.
    def enterOpt_block_label(self, ctx:PostgreSQLParser.Opt_block_labelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_block_label.
    def exitOpt_block_label(self, ctx:PostgreSQLParser.Opt_block_labelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_loop_label.
    def enterOpt_loop_label(self, ctx:PostgreSQLParser.Opt_loop_labelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_loop_label.
    def exitOpt_loop_label(self, ctx:PostgreSQLParser.Opt_loop_labelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_label.
    def enterOpt_label(self, ctx:PostgreSQLParser.Opt_labelContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_label.
    def exitOpt_label(self, ctx:PostgreSQLParser.Opt_labelContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_exitcond.
    def enterOpt_exitcond(self, ctx:PostgreSQLParser.Opt_exitcondContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_exitcond.
    def exitOpt_exitcond(self, ctx:PostgreSQLParser.Opt_exitcondContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#any_identifier.
    def enterAny_identifier(self, ctx:PostgreSQLParser.Any_identifierContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#any_identifier.
    def exitAny_identifier(self, ctx:PostgreSQLParser.Any_identifierContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#plsql_unreserved_keyword.
    def enterPlsql_unreserved_keyword(self, ctx:PostgreSQLParser.Plsql_unreserved_keywordContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#plsql_unreserved_keyword.
    def exitPlsql_unreserved_keyword(self, ctx:PostgreSQLParser.Plsql_unreserved_keywordContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#sql_expression.
    def enterSql_expression(self, ctx:PostgreSQLParser.Sql_expressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#sql_expression.
    def exitSql_expression(self, ctx:PostgreSQLParser.Sql_expressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expr_until_then.
    def enterExpr_until_then(self, ctx:PostgreSQLParser.Expr_until_thenContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expr_until_then.
    def exitExpr_until_then(self, ctx:PostgreSQLParser.Expr_until_thenContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expr_until_semi.
    def enterExpr_until_semi(self, ctx:PostgreSQLParser.Expr_until_semiContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expr_until_semi.
    def exitExpr_until_semi(self, ctx:PostgreSQLParser.Expr_until_semiContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expr_until_rightbracket.
    def enterExpr_until_rightbracket(self, ctx:PostgreSQLParser.Expr_until_rightbracketContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expr_until_rightbracket.
    def exitExpr_until_rightbracket(self, ctx:PostgreSQLParser.Expr_until_rightbracketContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expr_until_loop.
    def enterExpr_until_loop(self, ctx:PostgreSQLParser.Expr_until_loopContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expr_until_loop.
    def exitExpr_until_loop(self, ctx:PostgreSQLParser.Expr_until_loopContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#make_execsql_stmt.
    def enterMake_execsql_stmt(self, ctx:PostgreSQLParser.Make_execsql_stmtContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#make_execsql_stmt.
    def exitMake_execsql_stmt(self, ctx:PostgreSQLParser.Make_execsql_stmtContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#opt_returning_clause_into.
    def enterOpt_returning_clause_into(self, ctx:PostgreSQLParser.Opt_returning_clause_intoContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#opt_returning_clause_into.
    def exitOpt_returning_clause_into(self, ctx:PostgreSQLParser.Opt_returning_clause_intoContext):
        pass



del PostgreSQLParser