#!/usr/bin/env python
# coding: utf-8

# # chap02 스파크 간단히 살펴보기

# ### 2.5 spark session

# In[1]:


spark


# In[3]:


myRange = spark.range(500).toDF("number")


# ### 2.7 트랜스포메이션

# In[5]:


divisBy2 = myRange.where("number % 2 = 0")


# ### 2.8 액션

# In[6]:


divisBy2.count()


# ### 2.10 종합 예제

# In[7]:


flightData2015 = spark.read.option('inferSchema','true').option('header','true').csv('file:///home/ubuntu/study/spark/data/flight-data/csv/2015-summary.csv')


# In[8]:


flightData2015.take(3)


# In[10]:


flightData2015.sort('count').explain()


# In[11]:


# partition 수를 5개로 제한
spark.conf.set("spark.sql.shuffle.partitions","5")
flightData2015.sort('count').take(2)


# ### 2.10.1 DataFrame 과 SQL

# In[12]:


flightData2015.createOrReplaceTempView('flight_data_2015')


# In[13]:


sqlWay = spark.sql('''
SELECT DEST_COUNTRY_NAME, count(1)
FROM flight_data_2015
GROUP BY DEST_COUNTRY_NAME
''')


# In[14]:


dataFrameWay = flightData2015.groupBy('DEST_COUNTRY_NAME').count()


# In[15]:


sqlWay.explain()


# In[16]:


dataFrameWay.explain()


# #### 특정 위치를 왕래하는 최대 비행횟수를 구하기 위한 두가지 방법

# In[17]:


spark.sql("SELECT max(count) FROM flight_data_2015").take(1)


# In[18]:


from pyspark.sql.functions import max
flightData2015.select(max("count")).take(1)


# #### 도착지로 묶고 카운트의 합을 구하고 내림차순

# In[19]:


maxSql = spark.sql('''
SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
FROM flight_data_2015
GROUP BY DEST_COUNTRY_NAME
ORDER BY sum(count) DESC
LIMIT 5
''')
maxSql.show()


# In[21]:


from pyspark.sql.functions import desc

flightData2015.groupBy('DEST_COUNTRY_NAME').sum('count').withColumnRenamed("sum(count)", "destinational_total").sort(desc('destinational_total')).limit(5).show()

