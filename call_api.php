<?php


class APIcaller {
    public function callAPI($method, $url, $data = false) {
        $curl = curl_init();
        switch ($method) {
            case "POST":
                curl_setopt($curl, CURLOPT_POST, 1);
                if ($data) {
                    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
                }
                break;
            case "PATCH":
                curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PATCH");
                if ($data) {
                    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
                }
                break;
            case "DELETE":
                curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "DELETE");
                if ($data) {
                    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
                }
                break;
            default:
                if ($data) {
                    $url = sprintf("%s?%s", $url, http_build_query($data));
                }
        }
        // OPTIONS
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json',
            'permission: web_user'
        ));
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        // EXECUTE:
        $result = curl_exec($curl);
        if (!$result) {
            die("Connection Failure");
        }
        curl_close($curl);
        return $result;
    }
}

class APIinfo extends APIcaller {

    public function getInfos() {
        $url = "127.0.0.1:8000/api/infos/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getInfo($id) {
        $url = "127.0.0.1:8000/api/infos/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function deleteInfo($id) {
        $url = "127.0.0.1:8000/api/infos/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }

    public function updateInfo($id, $data) {
        $url = "127.0.0.1:8000/api/infos/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function createInfo($data) {
        $url = "127.0.0.1:8000/api/infos/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }
}


class APIGroupe extends APIcaller {

    public function getGroupes() {
        $url = "127.0.0.1:8000/api/groupes/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getGroupe($id) {
        $url = "127.0.0.1:8000/api/groupes/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function createGroupe($data) {
        $url = "127.0.0.1:8000/api/groupes/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }

    public function updateGroupe($id, $data) {
        $url = "127.0.0.1:8000/api/groupes/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function deleteGroupe($id) {
        $url = "127.0.0.1:8000/api/groupes/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }
}

class APIConcert extends APIcaller {

    public function getConcerts() {
        $url = "127.0.0.1:8000/api/concerts/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getConcert($id) {
        $url = "127.0.0.1:8000/api/concerts/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function createConcert($data) {
        $url = "127.0.0.1:8000/api/concerts/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }

    public function updateConcert($id, $data) {
        $url = "127.0.0.1:8000/api/concerts/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function deleteConcert($id) {
        $url = "127.0.0.1:8000/api/concerts/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }
}

class APIFestival extends APIcaller {
    
        public function getFestivals() {
            $url = "127.0.0.1:8000/api/festivals/";
            $response = $this->callAPI("GET", $url);
            $data = json_decode($response, true);
            return $data;
        }
    
        public function getFestival($id) {
            $url = "127.0.0.1:8000/api/festivals/$id/";
            $response = $this->callAPI("GET", $url);
            $data = json_decode($response, true);
            return $data;
        }
    
        public function createFestival($data) {
            $url = "127.0.0.1:8000/api/festivals/";
            $response = $this->callAPI("POST", $url, $data);
            $new_data = json_decode($response, true);
            return $new_data;
        }
    
        public function updateFestival($id, $data) {
            $url = "127.0.0.1:8000/api/festivals/$id/";
            $response = $this->callAPI("PATCH", $url, $data);
            $updated_data = json_decode($response, true);
            return $updated_data;
        }
    
        public function deleteFestival($id) {
            $url = "127.0.0.1:8000/api/festivals/$id/";
            $response = $this->callAPI("DELETE", $url);
            return $response;
        }
}

class APIAlbum extends APIcaller {
        
            public function getAlbums() {
                $url = "127.0.0.1:8000/api/albums/";
                $response = $this->callAPI("GET", $url);
                $data = json_decode($response, true);
                return $data;
            }
        
            public function getAlbum($id) {
                $url = "127.0.0.1:8000/api/albums/$id/";
                $response = $this->callAPI("GET", $url);
                $data = json_decode($response, true);
                return $data;
            }
        
            public function createAlbum($data) {
                $url = "127.0.0.1:8000/api/albums/";
                $response = $this->callAPI("POST", $url, $data);
                $new_data = json_decode($response, true);
                return $new_data;
            }
        
            public function updateAlbum($id, $data) {
                $url = "127.0.0.1:8000/api/albums/$id/";
                $response = $this->callAPI("PATCH", $url, $data);
                $updated_data = json_decode($response, true);
                return $updated_data;
            }
        
            public function deleteAlbum($id) {
                $url = "127.0.0.1:8000/api/albums/$id/";
                $response = $this->callAPI("DELETE", $url);
                return $response;
            }
}

$api_concert = new APIConcert();
var_dump($api_concert->getConcerts());

?>