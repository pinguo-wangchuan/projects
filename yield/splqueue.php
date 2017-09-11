<?php
/**
 * Created by PhpStorm.
 * User: wangchuan@camera360.com
 * Date: 2017/9/11
 * Time: 20:28
 */

$queue = new SplQueue();

/**
 * 可见队列和双链表的区别就是IteratorMode改变了而已，栈的IteratorMode只能为：
 * （1）SplDoublyLinkedList::IT_MODE_FIFO | SplDoublyLinkedList::IT_MODE_KEEP  （默认值,迭代后数据保存）
 * （2）SplDoublyLinkedList::IT_MODE_FIFO | SplDoublyLinkedList::IT_MODE_DELETE （迭代后数据删除）
 */

$queue->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO | SplDoublyLinkedList::IT_MODE_DELETE);

//SplQueue::enqueue()其实就是 SplDoublyLinkedList::push()
$queue->enqueue('a');
$queue->enqueue('b');
$queue->enqueue('c');

//SplQueue::dequeue()其实就是 SplDoublyLinkedList::shift()
var_dump($queue->dequeue());

foreach ($queue as $item) {
    echo $item . PHP_EOL;
}

print_r($queue);