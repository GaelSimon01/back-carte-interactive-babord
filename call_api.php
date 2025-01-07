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
            case "PUT":
                curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
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
        // OPTIONS:
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json',
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
        $url = "http://your-django-api-url/api/infos/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getInfo($id) {
        $url = "http://your-django-api-url/api/infos/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function deleteInfo($id) {
        $url = "http://your-django-api-url/api/infos/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }

    public function updateInfo($id, $data) {
        $url = "http://your-django-api-url/api/infos/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function createInfo($data) {
        $url = "http://your-django-api-url/api/infos/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }
}


class APIGroupe extends APIcaller {

    public function getGroupes() {
        $url = "http://your-django-api-url/api/groupes/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getGroupe($id) {
        $url = "http://your-django-api-url/api/groupes/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function createGroupe($data) {
        $url = "http://your-django-api-url/api/groupes/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }

    public function updateGroupe($id, $data) {
        $url = "http://your-django-api-url/api/groupes/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function deleteGroupe($id) {
        $url = "http://your-django-api-url/api/groupes/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }
}

class APIConcert extends APIcaller {

    public function getConcerts() {
        $url = "http://your-django-api-url/api/concerts/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function getConcert($id) {
        $url = "http://your-django-api-url/api/concerts/$id/";
        $response = $this->callAPI("GET", $url);
        $data = json_decode($response, true);
        return $data;
    }

    public function createConcert($data) {
        $url = "http://your-django-api-url/api/concerts/";
        $response = $this->callAPI("POST", $url, $data);
        $new_data = json_decode($response, true);
        return $new_data;
    }

    public function updateConcert($id, $data) {
        $url = "http://your-django-api-url/api/concerts/$id/";
        $response = $this->callAPI("PATCH", $url, $data);
        $updated_data = json_decode($response, true);
        return $updated_data;
    }

    public function deleteConcert($id) {
        $url = "http://your-django-api-url/api/concerts/$id/";
        $response = $this->callAPI("DELETE", $url);
        return $response;
    }
}

class APIFestival extends APIcaller {
    
        public function getFestivals() {
            $url = "http://your-django-api-url/api/festivals/";
            $response = $this->callAPI("GET", $url);
            $data = json_decode($response, true);
            return $data;
        }
    
        public function getFestival($id) {
            $url = "http://your-django-api-url/api/festivals/$id/";
            $response = $this->callAPI("GET", $url);
            $data = json_decode($response, true);
            return $data;
        }
    
        public function createFestival($data) {
            $url = "http://your-django-api-url/api/festivals/";
            $response = $this->callAPI("POST", $url, $data);
            $new_data = json_decode($response, true);
            return $new_data;
        }
    
        public function updateFestival($id, $data) {
            $url = "http://your-django-api-url/api/festivals/$id/";
            $response = $this->callAPI("PATCH", $url, $data);
            $updated_data = json_decode($response, true);
            return $updated_data;
        }
    
        public function deleteFestival($id) {
            $url = "http://your-django-api-url/api/festivals/$id/";
            $response = $this->callAPI("DELETE", $url);
            return $response;
        }
}

class APIAlbum extends APIcaller {
        
            public function getAlbums() {
                $url = "http://your-django-api-url/api/albums/";
                $response = $this->callAPI("GET", $url);
                $data = json_decode($response, true);
                return $data;
            }
        
            public function getAlbum($id) {
                $url = "http://your-django-api-url/api/albums/$id/";
                $response = $this->callAPI("GET", $url);
                $data = json_decode($response, true);
                return $data;
            }
        
            public function createAlbum($data) {
                $url = "http://your-django-api-url/api/albums/";
                $response = $this->callAPI("POST", $url, $data);
                $new_data = json_decode($response, true);
                return $new_data;
            }
        
            public function updateAlbum($id, $data) {
                $url = "http://your-django-api-url/api/albums/$id/";
                $response = $this->callAPI("PATCH", $url, $data);
                $updated_data = json_decode($response, true);
                return $updated_data;
            }
        
            public function deleteAlbum($id) {
                $url = "http://your-django-api-url/api/albums/$id/";
                $response = $this->callAPI("DELETE", $url);
                return $response;
            }
}

