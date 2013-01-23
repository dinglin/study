<?php
/**
 * 右值为常量
 */
//1：左值refcount=1,is_ref=0;
$a = str_repeat('-------',512*1024);
xdebug_debug_zval('a');
echo '1:'.memory_get_usage().chr(10);
#$a = 0;
unset($a);
xdebug_debug_zval('a');
echo '1:'.memory_get_usage().chr(10);

//2: 左值refcount>1,is_ref=0
$a = str_repeat('-------',512*1024);
$b = $a;
xdebug_debug_zval('a');
echo '2:'.memory_get_usage().chr(10);
#$a = 0;
unset($a);
xdebug_debug_zval('a');
echo '2:'.memory_get_usage().chr(10);

//3：左值refcount>1,is_ref=1
$a = str_repeat('-------',512*1024);
$b = &$a;
xdebug_debug_zval('a');
echo '3:'.memory_get_usage().chr(10);
#$a = 0;
unset($a);
xdebug_debug_zval('a');
echo '3:'.memory_get_usage().chr(10);

//4：特殊情况
$a = array(str_repeat('-------',512*1024));
$a[] = &$a;
xdebug_debug_zval('a');
echo '4:'.memory_get_usage().chr(10);
#$a = 0;
unset($a);
xdebug_debug_zval('a');
echo '4:'.memory_get_usage().chr(10);