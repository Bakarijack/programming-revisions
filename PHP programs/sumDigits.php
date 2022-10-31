<?php
$num = 14597;
$sum = 0; $remaining = 0;

for($i = 0;$i <= strlen($num);$i++){
    $remaining = $num % 10;
    $sum = $sum + $remaining;
    $num = $num / 10;
}

echo "Sum of the digits of 14597 is $sum";

?>