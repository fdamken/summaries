// Consumer.
void consumer() {
	int item;

	while (TRUE) {
		// Decrement full count or wait for new items.
		down(&full);

		// Ensure mutual exclusion and enter CS.
		down(&mutex);

		// Critical section (CS): Take item from buffer.
		item = remove_item();

		// Release the lock and leave CS.
		up(&mutex);

		// Increment count of empty slots.
		up(&empty);

		// Do something with the item.
		consume_item(item);
	}
}
