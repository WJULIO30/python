document,addEventListener('DOMContentLoaded', () => {

function hello(){
    console.log('hello wold');
}

hello();

function par(numero){
    return numero %2 === 0; //true ou false
}

var ePar = par(10)
console.log(ePar)

function soma(num1, num2){
    return num1 + num2     
    console.log(total);
}

const total= soma(12, 13);
console.log(total);

if(total >20){
    console.log('É maior que 20')
}else {
    console.log('É menor ou igual a 20');
}

/*
    Math.round(x) arredonda para o inteiro mais proximo
    Math.ceil(x) arredonda para cima cima para o inteiro mais proximo
    Math.floor(x)arredonda para baixo para o inteiro mais proximo
    Math.trunc(x) retorna a parte inteira de x
    Math.sign(x) retorna se x é negativo, null ou positivo
*/
function arrendondar(numero){
    return Math.round(numero);
}
console.log(arrendondar(7.9));
console.log(Math.sign(-99)); // retorna -1

const somaArrow = (num1, num2)=> {
    return num1 + num2
}

// OU 
// cont somaArrow = (nume1, nume2) => nume1 + num2;
    console.log(somaArrow(3,4));

    const arrIntegers = [1,2,3,4,5,6,7,8,9,10,11,]
    console.log(arrIntegers.length);
    console.log(arrIntegers[0]);
    console.log(arrIntegers[10]);

    const arrstrings = ['Gabriel' , 'SOFTGRAF' , 'Rafael'];
    console.log(arrIntegers[1]);

    const arrMisto = ['Gabriel' , 'SOFTGRAF' , 'Rafael', 1, 3, 7];

    console.log('Percorrendo o array com map');
    arrMisto.map(item => {
        console.log(item);
    });

    const novoArr = arrIntegers.map((item) =>{
        return item * 2;
    })
    console.log(novoArr);

    //percorre sem retornar um novo arry
    console.log('***percorrendo o array com foreach');
    arrIntegers.forEach((item) => {
        console.log(item);
    })
    console.log('***percorrendo o array com o for convencional');
    for (let i=0; i<arrIntegers.length; i++){
        console.log(arrIntegers[i]);
    }

    //objeto javascript
    const produto1 ={
        id: 1,
        descricao: 'Geladeira',
        preco: 2999,
        quant: 10
    };

    const produto2 ={
        id: 2,
        descricao: 'Cafeteira',
        preco: 199,
        quant: 20
    };
    const produto3 ={
        id: 3,
        descricao: 'Computador',
        preco: 7000,
        quant:5
    };

    const arrProdutos = [produto1, produto2];
    arrProdutos.push(produto3);

    console.log('*** Produto 1')
    console.log(arrProdutos[0].id);
    console.log(arrProdutos[0].descricao);
    console.log(arrProdutos[0].preco);
    console.log(arrProdutos[0].quant);

    console.log(arrProdutos);

    console.log('Filtrando produtos por preço:');
    const precoAcimaDe = arrProdutos.filter((produto) => produto.preco > 1000);
    console.log(precoAcimaDe);

    // remove o item da ultima posição
    const itemRemovido = arrProdutos.pop();
    console.log('Item removido: ' + itemRemovido.descricao);

    // remove item da primeira posição
    //const itemRemovido = arrProdutos.shift();
    //console.log('Item removido do inicio: ' + itemRemovido.descricao);

    // remove o item pela posição
    // const itemRemovido =arrProdutos.splice(1, 1); // (posicao, quantidade)
    // console.log(Item item removido pela posição: ' + arrProdutos);

    // busca produtos pelo indice para remover
    //const indice = arrProdutos.finIdex((produto) => produto.descricao == 'Geladeira');
    //console.log('Indice : ' indice);

    // verifica se todos os produtos tem preço acima de R$100 
    const todosPrecoAcimaDe = arrProdutos.some((produto) => produto.preco >= 1000);
    console.log(todosPrecoAcimaDe); //false

    // verifica de algum produto tem preço acima de R$1000
    const algumPrecoAcimaDe = arrProdutos.some((produto) => produto.preco >=1000);

    // soma a quantidade total de produtos em estoque 
    const somaQuant = arrProdutos.reduce((total, produto) => {
        return total + produto.quant;
    }, 0);
    console.log('total de produtos em estoque: ' + somaQuant);








});

