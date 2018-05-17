/*Funções usadas no arquivo cadastro.html*/

function validarTel() {
	var TxtTelefone = cadastro.TxtTelefone.value

	if (TxtTelefone.length != 8) {
		alert('Telefone fixo deve ter 8 dígitos!')
	}

	if( /[^0-9]/.test(TxtTelefone) ) {
		alert('Telefone deve conter apenas dígitos de 0 a 9!')
	}
}

function validarCel() {
	var TxtCelular = cadastro.TxtCelular.value

	if (TxtCelular.length != 9) {
		alert('Celular deve ter 9 dígitos!')
	}

	if( /[^0-9]/.test(TxtCelular) ) {
		alert('Celular deve conter apenas dígitos de 0 a 9!')
	}

}


/*Funções usadas no arquivo bicicletas.html*/

var biciModelo = new Array();
	biciModelo[0] = [ "MTB VOLT 1.6 PT/AM",
	                  "Bike_MTB_ARO16",
	                  "R$490,00" ];
	biciModelo[1] = [ "CALOL CECI BRANCA", 
	                  "Bike_Caloi_ARO16", 
	                  "R$469,00" ];
	biciModelo[2] = [ "POTI Branca/Vermelha", 
	                  "Bike_Poty_ARO26", 
	                  "R$489,00" ];
	biciModelo[3] = [ "CALOI Sport T19 V21 Marchas", 
	                  "Bike_Caloi_ARO26", 
	                  "R$880,00" ];

function Exibe( i ) {
    var desc = document.getElementById("desc");
    var foto = document.getElementById("foto");
    var preco = document.getElementById("preco");

    desc.innerHTML = biciModelo[i][0]
    foto.src = "imagens/" + biciModelo[i][1] + ".jpg";
    preco.innerHTML = biciModelo[i][2];
    }
    
function Esconde() {
    var desc = document.GetElementById("desc");
    var foto = document.GetElementById("foto");
    var preco = document.GetElementById("preco");

    desc.innerHTML = "";
    foto.src = "imagens/vazio.jpg";
    preco.innerHTML = "";
}

/*Funções usadas no arquivo pecas.html*/

function abrir(url) {
		window.open(url, "janela", "resizable=yes,width=400, height=600");
	}

/*Funções usadas no arquivo compras.html*/




function listaProdutos() {

var select = document.getElementById("selProduto")

var tipoProd = ["Guidom", "Selim", "Pedal", "Bike 16", "Bike 26"];

var detalhesProd = [
	[
    	["Alumínio CB Reforçado Polido", "R$ 35,00"],                      //tipoProd[0] 
    	["Alumínio Speed 31,8 X 420MM", "R$ 130,00"]
    ],
    [
    	["RAD 7 Comfort", "R$ 49,00"],                                     //tipoProd[1]
    	["SERFAS E-GEL DDMD-200", "R$ 199,00"]
    ],  
    [
    	["Inglês Alumínio", "R$ 27,00"]                                    //tipoProd[2]
    ],
    [
    	["MTB VOLT 1.6 PT/AM", "R$ 490,00"],                               //tipoProd[3]
    	["CALOL CECI BRANCA", "R$ 469,00"]
    ],
    [
    	["POTI Branca/Vermelha", "R$ 489,00"],                             //tipoProd[4]
    	["CALOI Sport T19 V21 Marchas", "R$ 880,00"]
    ]

    ]

	for (i = 0; i < tipoProd.length; i++) {
		var optgroup = document.createElement("optgroup");
		optgroup.label = tipoProd[i];
		var group_options = detalhesProd[i];
	
	for (j = 0; j < group_options.length; j++) {
		var option = document.createElement("option");
		option.text = group_options[j][0];
		option.value = j;
		optgroup.appendChild(option);
	}
	select.appendChild(optgroup);
	}
}

/*Tentativa questão 4c). Não funcionou :(

function adicionaItem() {

var select = document.getElementById("selProduto")
var option = option.text = group_options[j][0]
var textarea = document.getElementById("listaPedidos")
var button = document.getElementById("comprar")

var selectedProduct[i] = document.getElementById("selProduto".option).selectedIndex;

textarea.writeIn = selectedProduct[i]

}*/