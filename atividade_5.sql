SELECT  customer.customer_id,
	customer.first_name,
	customer.last_name,
	address.address_id,
FROM customer 
INNER JOIN address
ON customer.address_id=address.address_id 
-------------------------------------------
SELECT  film.title,
	film.film_id,
	category.name
FROM film
INNER JOIN film_category
ON film_category.film_id=film.film_id

INNER JOIN category
ON film_category.category_id=category.category_id
-------------------------------------------
SELECT  customer.customer_id,
	customer.first_name,
	customer.last_name,
	payment.payment_id,
	payment.amount,
	payment.payment_date
FROM customer
INNER JOIN payment
ON payment.customer_id=customer.customer_id
-------------------------------------------
SELECT  actor.actor_id,
	actor.first_anme,
	film.title,
	film.film_id,
FROM actor
INNER JOIN film_actor
ON film_actor.actor_id=actor.actor_id
INNER JOIN film
ON film.film_id=film_actor.film_id
-------------------------------------------
SELECT  staff.staff_id,
	staff.first_name,
	staff.last_name,
	address.address_id,
	store.store_id,
FROM address
INNER JOIN staff
ON staff.address_id=address.address_id
INNER JOIN store
ON store.address_id=address.address_id
-------------------------------------------



