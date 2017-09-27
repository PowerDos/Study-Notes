import { Injectable } from '@angular/core';

@Injectable()
export class StorageService {

    constructor() { }

    setItem(key, value){
        localStorage.setItem(key, JSON.stringify(value));
    }

    getItem(key){
        return JSON.parse(localStorage.getItem(key));
    }

    removeItem(key){
        localStorage.removeItem(key);
    }
}
