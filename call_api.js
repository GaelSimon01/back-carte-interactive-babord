class APICaller {
    async callAPI(method, url, data = null) {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch(url, options);
        const responseData = await response.json();
        return responseData;
    }
}



class APIAlbum extends APICaller {
    async getAlbums() {
        const url = 'http://86.218.243.242:8000/api/albums/';
        const response = await this.callAPI('GET', url);
        return response;
    }

    async getAlbum(id) {
        const url = `http://86.218.243.242:8000/api/albums/${id}/`;
        const response = await this.callAPI('GET', url);
        return response;
    }

    async createAlbum(data) {
        const url = 'http://86.218.243.242:8000/api/albums/';
        const response = await this.callAPI('POST', url, data);
        return response;
    }

    async updateAlbum(id, data) {
        const url = `http://86.218.243.242:8000/api/albums/${id}/`;
        const response = await this.callAPI('PATCH', url, data);
        return response;
    }
}

class APIFestival extends APICaller {
    async getFestivals() {
        const url = 'http://86.218.243.242:8000/api/festivals/';
        const response = await this.callAPI('GET', url);
        return response;
    }

    async getFestival(id) {
        const url = `http://86.218.243.242:8000/api/festivals/${id}/`;
        const response = await this.callAPI('GET', url);
        return response;
    }

    async createFestival(data) {
        const url = 'http://86.218.243.242:8000/api/festivals/';
        const response = await this.callAPI('POST', url, data);
        return response;
    }
}

class APIConcert extends APICaller {
    async getConcerts() {
        const url = 'http://86.218.243.242:8000/api/concerts/';
        const response = await this.callAPI('GET', url);
        return response;
    }

    async getConcert(id) {
        const url = `http://86.218.243.242:8000/api/concerts/${id}/`;
        const response = await this.callAPI('GET', url);
        return response;
    }

    async createConcert(data) {
        const url = 'http://86.218.243.242:8000/api/concerts/';
        const response = await this.callAPI('POST', url, data);
        return response;
    }

    async updateConcert(id, data) {
        const url = `http://86.218.243.242:8000/api/concerts/${id}/`;
        const response = await this.callAPI('PATCH', url, data);
        return response;
    }
}

class APIInfo extends APICaller {
    async getInfos() {
        const url = 'http://86.218.243.242:8000/api/infos/';
        const response = await this.callAPI('GET', url);
        return response;
    }

    async getInfo(id) {
        const url = `http://86.218.243.242:8000/api/infos/${id}/`;
        const response = await this.callAPI('GET', url);
        return response;
    }

    async deleteInfo(id) {
        const url = `http://86.218.243.242:8000/api/infos/${id}/`;
        const response = await this.callAPI('DELETE', url);
        return response;
    }

    async updateInfo(id, data) {
        const url = `http://86.218.243.242:8000/api/infos/${id}/`;
        const response = await this.callAPI('PATCH', url, data);
        return response;
    }
}

class APIGroupe extends APICaller {
    async getGroupes() {
        const url = 'http://86.218.243.242:8000/api/groupes/';
        const response = await this.callAPI('GET', url);
        return response;
    }

    async getGroupe(id) {
        const url = `http://86.218.243.242:8000/api/groupes/${id}/`;
        const response = await this.callAPI('GET', url);
        return response;
    }

    async createGroupe(data) {
        const url = 'http://86.218.243.242:8000/api/groupes/';
        const response = await this.callAPI('POST', url, data);
        return response;
    }

    async updateGroupe(id, data) {
        const url = `http://86.218.243.242:8000/api/groupes/${id}/`;
        const response = await this.callAPI('PATCH', url, data);
        return response;
    }

    async deleteGroupe(id) {
        const url = `http://86.218.243.242:8000/api/groupes/${id}/`;
        const response = await this.callAPI('DELETE', url);
        return response;
    }
}