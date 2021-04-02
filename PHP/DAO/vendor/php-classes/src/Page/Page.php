<?php

namespace Classes\Page;

use Rain\Tpl;

class Page{

    private $tpl;
    private $defaults = [

        "data"=>[]
    ];
    private $options;

    /*As variaveis viram de acorda com a rota*/

    public function __construct($opt = array())
    {


        //mescla dois arrays, onde o ultimo array sobrescreve os anteriores
        $this->options = array_merge($this->defaults, $opt);

        $config = array(
            "tpl_dir"       => $_SERVER["DOCUMENT_ROOT"]."/php_estudos/DAO/views/",
            "cache_dir"     => $_SERVER["DOCUMENT_ROOT"]."/php_estudos/DAO/cache/",
            "debug"         => false, // set to false to improve the speed
        );

        //var_dump($this->options);

        Tpl::configure($config);


        $this->tpl = new Tpl;

        $this->setData($this->options["data"]);

        $this->tpl->draw("header");
  
    }


    private function setData($opt = array())
    {
        foreach ($opt as $key => $value) {
            
            $this->tpl->assign($key,$value);
        }
    }

    //metodo para o html do conteudo

    public function setTpl($name, $data = array(), $returnHTML = false)
    {
        $this->setData($data);

        return $this->tpl->draw($name, $returnHTML);
    }

    public function __destruct()
    {

        $this->tpl->draw("footer");
    }

}
