---
title: spark_ml_01
date: 2018-01-24 17:28:33
tags:
---

# 特征正则
```
import org.apache.spark.ml.feature.Normalizer
import org.apache.spark.ml.linalg.Vectors

val dataFrame = spark.createDataFrame(Seq(
  (0, Vectors.dense(1.0, 0.5, -1.0)),
  (1, Vectors.dense(2.0, 1.0, 1.0)),
  (2, Vectors.dense(4.0, 10.0, 2.0))
)).toDF("id", "features")

// Normalize each Vector using $L^1$ norm.
val normalizer = new Normalizer()
  .setInputCol("features")
  .setOutputCol("normFeatures")
  .setP(1.0)

val l1NormData = normalizer.transform(dataFrame)
println("Normalized using L^1 norm")
l1NormData.show()

```

输出
```
+---+--------------+------------------+
| id|      features|      normFeatures|
+---+--------------+------------------+
|  0|[1.0,0.5,-1.0]|    [0.4,0.2,-0.4]|
|  1| [2.0,1.0,1.0]|   [0.5,0.25,0.25]|
|  2|[4.0,10.0,2.0]|[0.25,0.625,0.125]|
+---+--------------+------------------+

```


# 特征缩放
```
val dataFrame = spark.createDataFrame(Seq(
  (0, Vectors.dense(1.0, 2.0, 3.0)),
  (1, Vectors.dense(2.0, 2.0, 3.0)),
  (2, Vectors.dense(1.0, 2.0, 3.0))
)).toDF("id", "features")

val scaler = new StandardScaler()
  .setInputCol("features")
  .setOutputCol("scaledFeatures")
  .setWithStd(true)
  .setWithMean(false)
  
// Compute summary statistics by fitting the StandardScaler.
val scalerModel = scaler.fit(dataFrame)

// Normalize each feature to have unit standard deviation.
val scaledData = scalerModel.transform(dataFrame)
scaledData.show()
```

输出, 相同的列，缩放之后变为0
```
+-------------+--------------------+
|     features|      scaledFeatures|
+---+---------+--------------------+
|  0|[1.0,2.0,3.0]|[1.7320508075688774,0.0,0.0]|
| 1 |[2.0,2.0,3.0]|[3.464101615137755,0.0,0.0]|
|  3|[1.0,2.0,3.0]|[1.7320508075688774,0.0,0.0]]|
+---+---------+--------------------+


```