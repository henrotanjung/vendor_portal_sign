"use strict"

function onchangePekerjaan() {

    let pekerjaanElem = document.getElementById("pekerjaan");
    let pekerjaanLainnya = document.getElementById("pekerjaan_lainnya");
    if (pekerjaanElem.value === 'pekerjaan_lainnya') {
        pekerjaanLainnya.style.display = 'block';
    }
    if (pekerjaanElem.value !== 'pekerjaan_lainnya') {
        pekerjaanLainnya.style.display = 'none';
    }
}

function onchangeReff() {

    let reffElem = document.getElementById("referensi");
    let reffLainnya = document.getElementById("referensi_lainnya");
    if (reffElem.value === 'referensi_lainnya') {
        reffLainnya.style.display = 'block';
    }
    if (reffElem.value !== 'referensi_lainnya') {
        reffLainnya.style.display = 'none';
    }
}

