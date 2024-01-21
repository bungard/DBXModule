# Databricks notebook source
# COMMAND ----------
import Library.Functions as Func
#Will throw an error on both of these
Func.module1.m1A()
Func.module2.m2A()
# COMMAND ----------
import Library.Functions.module1 as Func1
#Func.module1 is now loaded
Func.module1.m1A()
Func.module2.m2A()
# COMMAND ----------
import Library.Functions.module2 as Func2
Func.module1.m1A()
#Func.module2 is now loaded
Func.module2.m2A()