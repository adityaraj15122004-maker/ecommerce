const productList = document.getElementById("product-list");

if (productList) {
    products.forEach(product => {
        productList.innerHTML += `
            <div class="product">
                <img src="${product.image}">
                <h3>${product.name}</h3>
                <p>₹${product.price}</p>
                <a href="pages/product.html?id=${product.id}">
                    <button>View Details</button>
                </a>
            </div>
        `;
    });
}

