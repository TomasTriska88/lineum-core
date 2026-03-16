<script lang="ts">
    import pkg from "../../package.json";
    import { ParaglideJS } from "@inlang/paraglide-sveltekit";
    import { i18n } from "$lib/i18n";

    import "../app.css";
    import ResonanceDeck from "$lib/components/ResonanceDeck.svelte";
    import CookieBanner from "$lib/components/CookieBanner.svelte";
    import Navigation from "$lib/components/Navigation.svelte";
    import ContactFooter from "$lib/components/ContactFooter.svelte";
    import { hudActive } from "$lib/stores/hudStore";
    import * as m from "$lib/paraglide/messages.js";
    import { page } from "$app/stores";

    $: isVoynich = $page.url.pathname.startsWith('/voynich');
</script>

<svelte:head>
    {#if isVoynich}
        <meta property="og:title" content="Voynich Object-Topology Archive | Lineum Lab" />
        <meta property="og:description" content="Structural analysis and interactive overlay for the Voynich Manuscript." />
    {:else}
        <meta property="og:title" content={m.meta_title()} />
        <meta property="og:description" content={m.meta_description()} />
    {/if}
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://lineum.io" />
    <meta property="og:image" content="https://lineum.io/social-preview.png" />
    <meta name="twitter:card" content="summary_large_image" />

    <script type="application/ld+json">
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": "Lineum Field Engine",
            "operatingSystem": "Any",
            "applicationCategory": "Systema Software",
            "description": "Continuous space particle dynamics simulator and API.",
            "offers": {
                "@type": "Offer",
                "price": "0"
            }
        }
    </script>
</svelte:head>

<ParaglideJS {i18n}>
    {#if !isVoynich}
        <Navigation />
        <div class="grid-bg"></div>
    {/if}

    <main class:hud-pushed={$hudActive && !isVoynich} class:is-voynich={isVoynich}>
        {#key $page.url.pathname}
            <slot />
        {/key}
    </main>

    {#if !isVoynich}
        <ResonanceDeck active={$hudActive} />
        <CookieBanner />
        <ContactFooter />
    {/if}
</ParaglideJS>

<style>
    main {
        position: relative;
        z-index: 1;
        padding-top: var(--nav-height, 120px);
        padding-bottom: 90px; /* Leave breathing room for the fixed Contact Footer */
        transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
    }

    main.hud-pushed {
        transform: translateY(-20px);
    }

    main.is-voynich {
        padding-top: 0;
        padding-bottom: 0;
    }

    @media (max-width: 768px) {
        main {
            padding-top: var(
                --nav-height,
                120px
            ); /* Standard padding is enough now */
        }
        main.is-voynich {
            padding-top: 0;
        }
    }
</style>
