#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	/* Create new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	/* If list is empty or new node should be first, insert at head */
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	/* Traverse the list to find the correct position for the new node */
	while (node && node->next && node->next->n < number)
		node = node->next;

	/* Insert the new node */
	new->next = node->next;
	node->next = new;

	return (new);
}

