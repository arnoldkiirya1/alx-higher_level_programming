#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	if (head == NULL)
		return 0;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return 1;
	}

	return 0;
}

