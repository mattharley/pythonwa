<template>
    <div class="max-w-4xl mx-auto">
        <div class="bg-white px-4 py-5 border-b border-gray-200 sm:px-6">
            <div class="-ml-4 -mt-2 flex items-center justify-between flex-wrap sm:flex-nowrap">
                <div class="ml-4 mt-2">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                        Upcoming Talks
                    </h3>
                </div>
                <div class="ml-4 mt-2 flex-shrink-0">
                    <button type="button" class="relative inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                        Apply to talk
                    </button>
                </div>
            </div>
        </div>
        <div class="bg-white shadow overflow-hidden sm:rounded-md">
            <ul class="divide-y divide-gray-200">
            <li v-for="talk in talks" :key="talk.link">
                <div class="flex items-center px-4 py-4 sm:px-6">
                    <div class="flex items-center">
                      <div class="px-4">
                          <div>
                            <a :href="talk.link" class="block hover:bg-gray-50">
                              <p class="font-medium text-blue-600 truncate">{{ talk.title }}</p>
                            </a>
                            <p class="mt-2 flex items-center text-sm text-gray-500">
                                <ClockIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                                <span class="truncate">{{ talk.time }}</span>
                            </p>
                            <p class="mt-2 flex items-center text-sm text-gray-500">
                                <LocationMarkerIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                                <span class="truncate">{{ talk.location }}</span>
                            </p>
                            <p class="mt-2 flex items-center text-sm text-gray-500">
                                <UserCircleIcon class="mr-1.5 h-5 w-5 text-gray-400" aria-hidden="true" />
                                <span class="truncate">{{ talk.attendance }}</span>
                            </p>
                            <p class="mt-2 flex items-center text-sm">
                                <span class="whitespace-pre-line" v-html="makeLinks(talk.description)"></span>
                            </p>
                          </div>
                      </div>
                    </div>
                </div>
            </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { ChatAlt2Icon, ClockIcon, LocationMarkerIcon, UserCircleIcon } from '@heroicons/vue/outline';

export default {
  components: {
    ChatAlt2Icon,
    ClockIcon,
    LocationMarkerIcon,
    UserCircleIcon
  },
  data() {
    return {
      talks: [
        {
          title: "Breaking the One Minute Mile - Adventures in Load Testing With Python",
          link: "https://www.meetup.com/pythonwa/events/279413063/",
          time: "AWST Thursday, 05 Aug 2021, 5:30 p.m. ( 2 weeks, 6 days from now )",
          location: "Riff @ Spacecubed",
          attendance: "15",
          description: `In December of 2015, the singer Adele placed all 50 shows of her international tour on sale at the same time on http://ticketmaster.com*
            This is what most would call a tactical error.

            After fan presales, a total of approximately 350,000^ tickets were sold in under 10 minutes. There was around 10M people (and 100k bots) all trying to buy tickets at once.

            Despite the load on the site, it did not crash although admittedly it slowed to a crawl and many people didn't realise until over an hour that tickets had sold out.

            So how can one deal with managing several high-volume ticketing sales? Well, the August talk will dive into just that with Matt Harley the Lead Developer for Megatix.

            An average of 35,000 tickets per minute seems like an unattainable feat for a small Perth-based ticketing company but with several high-volume sales coming up it was as good a time as any to finely tune the performance of their ticketing system to deal with a workload of that magnitude.

            Matt Harley is the Lead Developer at Megatix, a WA owned ticketing and events company and founder of Hipflask, an app which helps you find the coolest events around town.

            - https://megatix.com.au/
            - https://hipflaskapp.com

            * source: https://www.quora.com/What-was-the-quickest-time-in-history-tickets-for-a-show-concert-sold-out
            ^ The gross tickets was closer to 750k`
        }
      ]
    }
  },
  methods: {
    makeLinks(text) {
      return text;
    }
  }
};
</script>
