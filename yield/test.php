<?php
/**
 * Created by PhpStorm.
 * User: wangchuan@camera360.com
 * Date: 2017/9/9
 * Time: 9:35
 */
function gen()
{
    $yield1 = yield 'foo';
    var_dump($yield1);
    $yield2 = yield 'bar';
    var_dump($yield2);
}

$gen = gen();
var_dump($gen->send('something'));
var_dump($gen->send('test'));