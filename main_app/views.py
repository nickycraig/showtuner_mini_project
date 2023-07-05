from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .models import Composer, Show, Favorite
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context
    
class About(TemplateView):
    template_name = "about.html"

# class Composer:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

# composers = [
#     Composer("Stephen Sondheim", "https://static01.nyt.com/images/2022/01/26/obituaries/Sondheim-01/merlin_113967589_d0b46cc3-d3f4-49a4-b043-b4a9b26f3da6-superJumbo.jpg", "Regarded as one of the most important figures in 20th-century musical theater, he is credited for reinventing the American musical.With his frequent collaborations with Hal Prince and James Lapine, Sondheim's Broadway musicals tackled unexpected themes that ranged beyond the genre's traditional subjects, while addressing darker elements of the human experience.His music and lyrics were tinged with complexity, sophistication, and ambivalence about various aspects of life."),
#     Composer("Lin-Manuel Miranda","https://hips.hearstapps.com/hmg-prod/images/lin-manuel-miranda-macarthur-via-wikicommons_1000.jpg", "He is known for creating the Broadway musicals In the Heights (2005), and Hamilton (2015), and the soundtracks for the animated films Moana (2016), Encanto, and Vivo (both 2021). His awards include three Tony Awards, two Emmy Awards, five Grammy Awards, two Laurence Olivier Awards, an Annie Award, a MacArthur Fellowship Award, a Kennedy Center Honor, and a Pulitzer Prize."),
#     Composer("Cole Porter", "https://hips.hearstapps.com/hmg-prod/images/gettyimages-3305347-copy.jpg", "Born to a wealthy family in Indiana, Porter defied his grandfather's wishes for him to practice law and took up music as a profession. Classically trained, he was drawn to musical theatre. After a slow start, he began to achieve success in the 1920s, and by the 1930s he was one of the major songwriters for the Broadway musical stage."),
#     Composer("Jeanine Tesori", "https://www.theintervalny.com/wp-content/uploads/2015/09/Screen-Shot-2016-02-10-at-10.43.29-AM.png", "She is the most prolific and honored female theatrical composer in history, with five Broadway musicals and six Tony Award nominations.She won the 1999 Drama Desk Award for Outstanding Music in a Play for Nicholas Hytner's production of Twelfth Night at Lincoln Center, the 2004 Drama Desk Award for Outstanding Music for Caroline, or Change, the 2015 Tony Award for Best Original Score for Fun Home (shared with Lisa Kron), making them the first female writing team to win that award, and the 2023 Tony Award for Best Original Score for Kimberly Akimbo (shared with David Lindsay-Abaire).She was named a Pulitzer Prize for Drama finalist twice for Fun Home and Soft Power."),
#     Composer("Richard Rodgers", "https://www.seattlechambermusic.org/wp-content/uploads/richard-rodgers-37431-1-402.jpg", "Rodgers is known for his songwriting partnerships, first with lyricist Lorenz Hart and then with Oscar Hammerstein II. With Hart he wrote musicals throughout the 1920s and 1930s, including Pal Joey, A Connecticut Yankee, On Your Toes and Babes in Arms. With Hammerstein he wrote musicals through the 1940s and 1950s, such as Oklahoma!, Flower Drum Song, Carousel, South Pacific, The King and I, and The Sound of Music. His collaborations with Hammerstein, in particular, are celebrated for bringing the Broadway musical to a new maturity by telling stories that were focused on characters and drama rather than the earlier light-hearted entertainment of the genre."),
#     Composer("Alan Menken", "https://static.wikia.nocookie.net/disney/images/5/5e/Alan_Menken.jpg/revision/latest/zoom-crop/width/500/height/500?cb=20200607014723", "American composer, pianist, singer, music director, and record producer, best known for his scores and songs for films produced by Walt Disney Animation Studios. Menken's music for The Little Mermaid (1989), Beauty and the Beast (1991), Aladdin (1992), and Pocahontas (1995) has each won him two Academy Awards. He also composed the scores and songs for Little Shop of Horrors (1986), Newsies (1992), The Hunchback of Notre Dame (1996), Hercules (1997), Home on the Range (2004), Enchanted (2007), Tangled (2010), and Disenchanted (2022), among others.")
# ]

class ComposerList(TemplateView):
    template_name = "composer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["composers"] =  Composer.objects.filter(name__icontains=name)
        else:
            context["composers"] = Composer.objects.all()
        return context
    
class ComposerCreate(CreateView):
    model = Composer
    fields = ['name', 'image', 'bio', 'verified_artist']
    template_name = "composer_create.html"
    def get_success_url(self):
        return reverse('composer_detial', kwargs={'pk': self.object.pk})

class ComposerDetail(DetailView):
    model = Composer
    template_name = "composer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

class ComposerUpdate(UpdateView):
    model = Composer
    fields = ['name', 'image', 'bio', 'verified_artist']
    template_name = "composer_update.html"
    def get_success_url(self):
        return reverse('composer_detial', kwargs={'pk': self.object.pk})

class ComposerDelete(DeleteView):
    model = Composer
    template_name = "composer_delete_confirmation.html"
    success_url = "/composers/"

class ShowCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        year = request.POST.get("year")
        composer = Composer.objects.get(pk=pk)
        Show.objects.create(title=title, year=year, composer=composer)
        return redirect('composer_detail', pk=pk)
    
class FavoriteShowAssoc(View):
    def get(self, request, pk, show_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Favorite.objects.get(pk=pk).shows.remove(show_pk)
        if assoc == "add":
            Favorite.objects.get(pk=pk).shows.add(show_pk)
        return redirect('home')