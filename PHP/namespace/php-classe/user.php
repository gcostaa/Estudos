<?php

class user{


    private $nome;

    public function getNome()
    {
        return $this->nome;
    }

    public function setNome(string $nome)
    {

        $this->nome = $nome; 
    
    }

    public static function faz()
    {
        echo "faz merda";
    }


    public function __toString()
    {
       return json_encode($this->getNome());
    }
}