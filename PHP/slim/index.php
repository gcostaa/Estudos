<?php

require_once ("Page.php");
require_once ("vendor/autoload.php");

use Slim\Slim;
use Rain\Tpl;
// config

//$app configura cada uma das rotas
$app = new Slim();

$app->get('/hello/:name', function ($name) {
    echo "Hello, " . $name;
});

$app->get('/', function () {

    /*$config = array(
        "tpl_dir"       => "tpl/",
        "cache_dir"     => "cache/",
        "debug"         => false, // set to false to improve the speed
    );
    
    Tpl::configure( $config );
    
    $tpl = new Tpl;

    $tpl->assign( "name", "Gustavo" );
    $tpl->draw("index");*/

    $page = new Page();

	$page->setTpl("index");

});


$app->run();