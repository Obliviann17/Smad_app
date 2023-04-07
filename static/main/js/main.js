const cartItems = [];

		function addToCart(productName) {
			cartItems.push(productName);
			updateCart();
		}

		function updateCart() {
			const cartList = document.getElementById('cart-items');
			cartList.innerHTML = '';
			cartItems.forEach((item) => {
				const li = document.createElement('li');
				li.textContent = item;
				cartList.appendChild(li);
			});
		}