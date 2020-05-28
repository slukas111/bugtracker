from django.shortcuts import render

# Create your views here.
def ticket(request, ticket_id):
	ticket = Ticket.objects.get(pk=int(ticket_id))
	if request.method == 'POST':

		if form.is_valid():
			ticket =  Ticket.objects.get(pk=int(ticket_id))


				# recipient_list = (ticket.submitter_email, )
				# send_mail(subject, message, from_email, recipient_list)
			comment.save()
            return render(request, "home.html")