// Producer.
void producer() {
	int item;

	while (TRUE) {
		item = produce_item();

		// Decrement empty count or wait for free slots.
		down(&empty);

		// Ensure mutual exclusion and enter CS.
		down(&mutex);

		// Critical section (CS): Insert item into buffer.
		insert_item(item);

		// Release the lock and leave CS.
		up(&mutex);

		// Increment count of full slots.
		up(&full);
	}
}
