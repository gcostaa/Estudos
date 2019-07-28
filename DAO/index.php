<?php

require 'vendor/autoload.php';

use \Slim\Slim;
use \Classes\Model\db\Sql;
use \Classes\Page\Page;

$app = new Slim;

$app->get('/', function () {

    echo "<h1>Acesse o admin</h1>";

});

$app->get('/admin', function () {

    $page = new Page();

    $page->setTpl("index");

});

$app->get('/admin/user', function () {

    $page = new Page();

    $page->setTpl("users");

});


$app->get('/admin/user/create', function () {

    $page = new Page();

    $page->setTpl("users-create");

});

$app->get('/admin/user/select', function () {

   $sql = new Sql();

   echo $sql->loadbyId(17,"iduser","tb_users");

});




$app->run();