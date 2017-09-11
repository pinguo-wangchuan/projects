<?php
function xrange($start, $end, $step = 1)
{
    for ($i = $start; $i <= $end; $i += $step) {
        yield $i;
    }
}

$a = xrange(1, 1000000);
/*
foreach ($a as $num) {
    echo $num, "\n";
}
*/

function logger($fileName)
{
    $fileHandle = fopen($fileName, 'a');
    while (true) {
        fwrite($fileHandle, yield . "\n");
    }
}

/*$logger = logger(__DIR__ . '/log');
echo __DIR__ . '/log';
var_dump(get_class_methods($logger));
$logger->send('Foo');
$logger->send('Bar');*/

function gen()
{
    $ret = (yield 'yield1');
    var_dump($ret);
    $ret = (yield 'yield2');
    var_dump($ret);
    $ret = (yield 'yield3');
    //var_dump($ret);
}

$gen = gen();
//var_dump($gen->current());
var_dump($gen->send('ret1'));
var_dump($gen->send('ret2'));
var_dump($gen->current());
?>