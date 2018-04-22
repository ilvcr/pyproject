1->
    图像配准是对图像进行变换，使变换后的图像能够在常见的坐标系中对齐。
        配准可以是严格配准，也可以是非严格配准。
    
2->
    为了能够进行图像对比和更精细的图像分析，图像配准是一步非常重要的操作。


3->
    jkface.xml


<?xml version="1.0" encoding="utf-8"?>
<faces>
<face file="jk-002.jpg" xf="46" xm="56" xs="67" yf="38" ym="65" ys="39"/>
<face file="jk-006.jpg" xf="38" xm="48" xs="59" yf="38" ym="65" ys="38"/>
<face file="jk-004.jpg" xf="40" xm="50" xs="61" yf="38" ym="66" ys="39"/>
<face file="jk-010.jpg" xf="33" xm="44" xs="55" yf="38" ym="65" ys="38"/>
…
</faces>


4->
    如果存在更多的对应点对，其计算公式相同，只需在矩阵中额外添加几行。
        你可以使用 linalg.lstsq() 函数来计算该问题的最小二乘解。 

