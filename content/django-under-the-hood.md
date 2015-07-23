title: Django under the hood
Status: draft
Category: django
Tags: python, django, conferences
Date: 2014-11-18


Well the tickets sold in just 20 seconds and I can see why. [Django under the hood](http://www.djangounderthehood.com/) was a fun and informative dive into Django's innards. The conference was billed as *an exciting new Django conference for experienced Django developers* to *come and learn about the internals of Django, and help to shape its future* so clearly expanding the existing contributor base was a main part of the mission here. And I think it's fair to say it's proved the viability of a technical conference used to disseminate specific internal knowledge to a wider group.

# The talks

I'm planning to give a summary of the talks at work, so I'm collecting some notes on the talks here.

## Django ORM - [Anssi Kääriäinen](https://github.com/akaariai)

The recognised expert of the ORM, Anssi gave us a tour of a couple of the recent and upcoming features of Django's database wrapper. These features both add to the filtering capability of the ORM.

He started with [field transformations](https://docs.djangoproject.com/en/1.7/howto/custom-lookups/#a-simple-transformer-example) (new in 1.7). These enable a database value to be transformed before an evaluation is made. The example he gave was:

    Book.objects.filter(author__birth_date__year__lte=1981)

Now you may have suspected this already works in Django, but not so. You'll get this error:

    FieldError: Unsupported lookup 'year' for DateTimeField or join on the field not permitted.

This `year` part is exactly the added link of the chain avaiable with the new [django.db.models.Transform](https://docs.djangoproject.com/en/1.7/ref/models/lookups/#django.db.models.Transform) class:

    from django.db.models import Transform, DateField, IntegerField

    @DateField.register_lookup
    class YearTransform(Transform):
        lookup_name = 'year'
        output_field = IntegerField()

        def as_sql(self, compiler, connection):
            lhs, params = compiler.compile(self.lhs)
            return "EXTRACT(YEAR FROM %s)" % lhs, params

And now the query works:

    >>> Book.objects.filter(author__birth_date__year__lte=1981)
    [<Book from 1980>, <Book from 1945>]

We expect obvious date time lookups like these to be built into Django in future, but there'll always be more demanding cases, where transforms will now be available. Take the example of filtering by *length of string*, previously this [had to be done like this](http://stackoverflow.com/a/19296333/15890):

    MyModel.objects.extra(where=["CHAR_LENGTH(text) > 300"])

And I think that's really the point of transforms and other new ORM features: removing the need for `.raw` and `.extra`.

Next Anssi looked at ... RunSQL
[custom-lookups](https://docs.djangoproject.com/en/1.7/howto/custom-lookups/).

http://reinout.vanrees.org/weblog/2014/11/14/1django-orm.html

## Django migrations framework
Andrew Godwin

## Django Rest Framework
Tom Christie

## Internationalisation
Jannis Leidel

## Model._meta
Daniel Pyrathon

## Python templating
Armin Ronacher




Tech talks worked

Feedback email: structured sprints. Advertise what's needed. Organise groups.