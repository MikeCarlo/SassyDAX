# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

df = "test"
df2 = "moretest"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%run /SassyDAX_final_final_v02

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

SassyDAX.analyzeDF(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

SassyDAX.analyzeDF(df2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

SassyDAX.relationships("my Model Name")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ![image-alt-text](https://www.reddit.com/r/PowerBI/comments/1bz3djx/does_this_look_right_to_yall_its_my_first_data/#lightbox)

# CELL ********************

SassyDAX.modelImage('https://onelake.dfs.fabric.microsoft.com/FabCon2024/lake01.Lakehouse/Files/imgs/semantic model.png')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

SassyDAX.BPA('ModelName')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

SassyDAX.exportToExcel('WorkspaceName/ModelName')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
