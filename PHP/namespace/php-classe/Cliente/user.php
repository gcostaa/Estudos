<?php

namespace Cliente;

class user extends \user{

    public function registraVenda()
    {
        echo "Foi vendido para". $this->getNome();
    }
    
}