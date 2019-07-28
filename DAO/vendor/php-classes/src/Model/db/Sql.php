<?php

namespace Classes\Model\db;

//ela extender faz com que sql tenha acesso a tudo de \PDO
class Sql extends \PDO {

    private $con;
    private const DB = "db_ecommerce";
    private const USER = "root";
    private const SENHA = "";

    public function __construct()

    {
        $this->con = new \PDO("mysql:host=localhost;dbname=". self::DB, self::USER, self::SENHA);

        //echo "conect";    
    }

    /*
    $stmt = $con->prepare("INSERT INTO pessoa(nome, email) VALUES(?, ?)");
    $stmt->bindParam(1,”Nome da Pessoa”);
    $stmt->bindParam(2,”email@email.com”);
    */
    private function setParams($statment, $parameters = array()){
        
        foreach ($parameters as $key => $value) {
            
            $this->setParam($statment,$key,$value);
        }
    }

    private function setParam($statment, $key, $value){

            $statment->bindParam($key, $value);
    }

   
    //prepara a query utiliza os metodos acima
    public function query($rawQuery, $params = array())
    {
        $stmt = $this->con->prepare($rawQuery);

        $this->setParams($stmt, $params);

        $stmt->execute();
   
        return $stmt;
        
    }

    public function select($rowQuery, $params = array()):array
    {
        $stmt = $this->query($rowQuery, $params);
        //fecthAll esta no stmt
        return $stmt->fetchAll(\PDO::FETCH_ASSOC);

    }

    public function insertcomp($table, $data = array())
    {
        $campos = [];

        $stmt = $this->query("SHOW COLUMNS FROM $table", array());

        $result = $stmt->fetchAll(\PDO::FETCH_ASSOC);

        for ($i=0; $i < count($result) ; $i++) { 
    
            $campos[$i]= $result[$i]["Field"];
            
        }

        (int) $cont = 0;

        $rowQuery = "INSERT INTO $table VALUES :".implode($campos,", :").";";

        foreach ($campos as $key) {

            $campos[$key] = $data[$cont];

            $cont++;
            
        }

        array_splice($campos, 0, 6);

        echo json_encode($campos);
       
        $this->query($rowQuery, $data);

        
    }

    public function insert($table, $dados = array())
    {
        $this->query("INSERT INTO $table VALUES 
        (null,:idperson,:deslogin, :despassword, :inadmin, null)", $dados);
    }

    public function loadbyId($id, $primary_key, $tb)
    {
        $stmt = $this->query("SELECT * FROM $tb WHERE $primary_key = :id", array(":id"=>$id));

        return json_encode($stmt->fetchAll(\PDO::FETCH_ASSOC));
    }

    public function delete($id, $primary_key, $tb)
    {
        $this->query("DELETE FROM $tb WHERE $primary_key = :id", array(":id"=>$id));
    }

    public function update($id, $tb, $primary_key, $campo, $valor)
    {
        $this->query("UPDATE $tb SET $campo = :valor where $primary_key = :id;", 
        array(

            ":valor"=>$valor,
            ":id"=>$id
                 
        ));
    }
}




